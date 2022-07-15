"""Schema parsing tests"""
from bids_pydantic.schema_parsing import (
    YAML_HEADER_BLOCK,
    adjust_references,
    find_first_non_comment_line,
    indent_all_lines,
    insert_yaml_header,
    prepare_yaml_metadata_text,
)


def test_find_first_non_comment_line() -> None:
    """Test that we can find the first non-comment line in a YAML file.
    Excludes anything starting with --- or #"""
    assert (
        find_first_non_comment_line(
            """---
# comment
  #comment

     line"""
        )
        == 4
    )
    assert (
        find_first_non_comment_line(
            """  ---
# comment
  #comment
--- something


     findthisline# ---
     not this one"""
        )
        == 6
    )


def test_indent_all_lines() -> None:
    """Test that string blocks can be indented from a given line"""
    assert (
        indent_all_lines(
            """---
abc
 def
  ghi""",
            from_line=2,
            indent=2,
        )
        == """---
abc
   def
    ghi"""
    )


def test_insert_yaml_header() -> None:
    """Test that the YAML header is successfully inserted"""
    assert (
        insert_yaml_header(
            """#something
---
   #else
     #indent
insert above
ok"""
        )
        == """#something
---
   #else
     #indent"""
        + YAML_HEADER_BLOCK
        + """insert above
ok"""
    )


def test_adjust_references() -> None:
    """Test that `$ref: something` is converted to $ref: #/something"""
    assert (
        adjust_references(
            """
something
properties:
  anyOf:
    - $ref: _MEGCoordSys
       - $ref: _EEGCoordSys
  blah:
    - $ref: _StandardTemplateCoordSys"""
        )
        == """
something
properties:
  anyOf:
    - $ref: #/_MEGCoordSys
       - $ref: #/_EEGCoordSys
  blah:
    - $ref: #/_StandardTemplateCoordSys"""
    )


def test_yaml_conversion() -> None:
    """Test the full YAML conversion is successful"""
    input_text = r"""---
# Some
  # Comments (w/ whitespace)
AProperty:
  name: AProperty
  description: |
    A description
  anyOf:
  - $ref: _MEGCoordSys
  - $ref: Genetics.Dataset"""
    assert (
        prepare_yaml_metadata_text(input_text)
        == r"""---
# Some
  # Comments (w/ whitespace)"""
        + YAML_HEADER_BLOCK
        + """  AProperty:
    name: AProperty
    description: |
      A description
    anyOf:
    - $ref: #/_MEGCoordSys
    - $ref: #/Genetics.Dataset"""
    )
