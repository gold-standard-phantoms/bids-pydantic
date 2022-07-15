# Generated using BIDS-pydantic v0.0.1 using BIDS schema v1.7.0
# from https://raw.githubusercontent.com/bids-standard/bids-specification/v1.7.0/src/schema/objects/metadata.yaml
# Uses datamodel-code-generator v0.13.0
from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field, PositiveFloat, confloat, conint, constr


class AcquisitionVoxelSizeItem(BaseModel):
    __root__: PositiveFloat


class AnatomicalLandmarkCoordinateUnits(Enum):
    """
    Units of the coordinates of `"AnatomicalLandmarkCoordinateSystem"`.

    """

    m = "m"
    mm = "mm"
    cm = "cm"
    n_a = "n/a"


class ArterialSpinLabelingType(Enum):
    """
    The arterial spin labeling type.

    """

    CASL = "CASL"
    PCASL = "PCASL"
    PASL = "PASL"


class CASLType(Enum):
    """
    Describes if a separate coil is used for labeling.

    """

    single_coil = "single-coil"
    double_coil = "double-coil"


class ChunkTransformationMatrixItem(BaseModel):
    __root__: List[Any]


class ChunkTransformationMatrixItem1(BaseModel):
    __root__: List[Any]


class ContrastBolusIngredient(Enum):
    """
        Active ingredient of agent.
    Corresponds to DICOM Tag 0018, 1048 `Contrast/Bolus Ingredient`.

    """

    IODINE = "IODINE"
    GADOLINIUM = "GADOLINIUM"
    CARBON_DIOXIDE = "CARBON DIOXIDE"
    BARIUM = "BARIUM"
    XENON = "XENON"


class DatasetType(Enum):
    """
        The interpretation of the dataset.
    For backwards compatibility, the default value is `"raw"`.

    """

    raw = "raw"
    derivative = "derivative"


class DigitizedHeadPointsCoordinateUnits(Enum):
    """
    Units of the coordinates of `"DigitizedHeadPointsCoordinateSystem"`.

    """

    m = "m"
    mm = "mm"
    cm = "cm"
    n_a = "n/a"


class EEGCoordinateUnits(Enum):
    """
    Units of the coordinates of `EEGCoordinateSystem`.

    """

    m = "m"
    mm = "mm"
    cm = "cm"
    n_a = "n/a"


class FiducialsCoordinateUnits(Enum):
    """
        Units in which the coordinates that are  listed in the field
    `"FiducialsCoordinateSystem"` are represented.

    """

    m = "m"
    mm = "mm"
    cm = "cm"
    n_a = "n/a"


class Container(BaseModel):
    Type: Optional[str] = None
    Tag: Optional[str] = None
    URI: Optional[AnyUrl] = None


class GeneratedByItem(BaseModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    Description: Optional[str] = None
    CodeURL: Optional[AnyUrl] = None
    Container: Optional[Container] = None


class Genetics(BaseModel):
    """
    An object containing information about the genetics descriptor.

    """

    Database: Optional[Any] = None
    Dataset: Optional[Any] = None
    Descriptors: Optional[Any] = None


class HardwareFilter(Enum):
    n_a = "n/a"


class HeadCoilCoordinateUnits(Enum):
    """
    Units of the coordinates of `HeadCoilCoordinateSystem`.

    """

    m = "m"
    mm = "mm"
    cm = "cm"
    n_a = "n/a"


class InjectedMas(Enum):
    n_a = "n/a"


class InjectedMassUnit(Enum):
    n_a = "n/a"


class M0Type(Enum):
    """
        Describes the presence of M0 information.
    `"Separate"` means that a separate `*_m0scan.nii[.gz]` is present.
    `"Included"` means that an m0scan volume is contained within the current
    `*_asl.nii[.gz]`.
    `"Estimate"` means that a single whole-brain M0 value is provided.
    `"Absent"` means that no specific M0 information is present.

    """

    Separate = "Separate"
    Included = "Included"
    Estimate = "Estimate"
    Absent = "Absent"


class MEGCoordinateUnits(Enum):
    """
    Units of the coordinates of `"MEGCoordinateSystem"`.

    """

    m = "m"
    mm = "mm"
    cm = "cm"
    n_a = "n/a"


class MRAcquisitionType(Enum):
    """
        Type of sequence readout.
    Corresponds to DICOM Tag 0018, 0023 `MR Acquisition Type`.

    """

    field_2D = "2D"
    field_3D = "3D"


class MTPulseShape(Enum):
    """
        Shape of the magnetization transfer RF pulse waveform.
    The value `"GAUSSHANN"` refers to a Gaussian pulse with a Hanning window.
    The value `"SINCHANN"` refers to a sinc pulse with a Hanning window.
    The value `"SINCGAUSS"` refers to a sinc pulse with a Gaussian window.

    """

    HARD = "HARD"
    GAUSSIAN = "GAUSSIAN"
    GAUSSHANN = "GAUSSHANN"
    SINC = "SINC"
    SINCHANN = "SINCHANN"
    SINCGAUSS = "SINCGAUSS"
    FERMI = "FERMI"


class MeasurementToolMetadata(BaseModel):
    """
        A description of the measurement tool as a whole.
    Contains two fields: `"Description"` and `"TermURL"`.
    `"Description"` is a free text description of the measurement tool.
    `"TermURL"` is a URL to an entity in an ontology corresponding to this tool.

    """

    TermURL: Optional[AnyUrl] = None
    Description: Optional[str] = None


class PCASLType(Enum):
    """
    The type of gradient pulses used in the `control` condition.

    """

    balanced = "balanced"
    unbalanced = "unbalanced"


class PhaseEncodingDirection(Enum):
    """
        The letters `i`, `j`, `k` correspond to the first, second and third axis of
    the data in the NIFTI file.
    The polarity of the phase encoding is assumed to go from zero index to
    maximum index unless `-` sign is present
    (then the order is reversed - starting from the highest index instead of
    zero).
    `PhaseEncodingDirection` is defined as the direction along which phase is was
    modulated which may result in visible distortions.
    Note that this is not the same as the DICOM term
    `InPlanePhaseEncodingDirection` which can have `ROW` or `COL` values.

    """

    i = "i"
    j = "j"
    k = "k"
    i_ = "i-"
    j_ = "j-"
    k_ = "k-"


class PixelSizeItem(BaseModel):
    __root__: confloat(ge=0.0)


class PixelSizeUnits(Enum):
    """
        Unit format of the specified `"PixelSize"`. MUST be one of: `"mm"` (millimeter), `"um"`
    (micrometer) or `"nm"` (nanometer).

    """

    mm = "mm"
    um = "um"
    nm = "nm"


class PowerLineFrequencyEnum(Enum):
    n_a = "n/a"


class RecordingType(Enum):
    """
        Defines whether the recording is `"continuous"`, `"discontinuous"`, or
    `"epoched"`, where `"epoched"` is limited to time windows about events of
    interest (for example, stimulus presentations or subject responses).

    """

    continuous = "continuous"
    epoched = "epoched"
    discontinuous = "discontinuous"


class SampleEnvironment(Enum):
    """
        Environment in which the sample was imaged. MUST be one of: `"in vivo"`, `"ex vivo"`
    or `"in vitro"`.

    """

    in_vivo = "in vivo"
    ex_vivo = "ex vivo"
    in_vitro = "in vitro"


class SampleOrigin(Enum):
    """
    Describes from which tissue the genetic information was extracted.

    """

    blood = "blood"
    saliva = "saliva"
    brain = "brain"
    csf = "csf"
    breast_milk = "breast milk"
    bile = "bile"
    amniotic_fluid = "amniotic fluid"
    other_biospecimen = "other biospecimen"


class SliceEncodingDirection(Enum):
    """
        The axis of the NIfTI data along which slices were acquired,
    and the direction in which `"SliceTiming"` is defined with respect to.
    `i`, `j`, `k` identifiers correspond to the first, second and third axis of
    the data in the NIfTI file.
    A `-` sign indicates that the contents of `"SliceTiming"` are defined in
    reverse order - that is, the first entry corresponds to the slice with the
    largest index, and the final entry corresponds to slice index zero.
    When present, the axis defined by `"SliceEncodingDirection"` needs to be
    consistent with the `slice_dim` field in the NIfTI header.
    When absent, the entries in `"SliceTiming"` must be in the order of increasing
    slice index as defined by the NIfTI header.

    """

    i = "i"
    j = "j"
    k = "k"
    i_ = "i-"
    j_ = "j-"
    k_ = "k-"


class SoftwareFilter(Enum):
    n_a = "n/a"


class SourceDataset(BaseModel):
    URL: Optional[AnyUrl] = None
    DOI: Optional[str] = None
    Version: Optional[str] = None


class SpatialReferenceEnum(Enum):
    orig = "orig"


class SpatialReferenceEnum1(Enum):
    orig = "orig"


class SpecificRadioactivityEnum(Enum):
    n_a = "n/a"


class SpecificRadioactivityUnit(Enum):
    n_a = "n/a"


class SpoilingType(Enum):
    """
    Specifies which spoiling method(s) are used by a spoiled sequence.

    """

    RF = "RF"
    GRADIENT = "GRADIENT"
    COMBINED = "COMBINED"


class StimulusPresentation(BaseModel):
    """
        Object containing key value pairs related to the software used to present
    the stimuli during the experiment, specifically:
    `"OperatingSystem"`, `"SoftwareName"`, `"SoftwareRRID"`, `"SoftwareVersion"` and
    `"Code"`.
    See table below for more information.

    """

    OperatingSystem: Optional[Any] = None
    SoftwareName: Optional[Any] = None
    SoftwareRRID: Optional[Any] = None
    SoftwareVersion: Optional[Any] = None
    Code: Optional[Any] = None


class TissueOrigin(Enum):
    """
    Describes the type of tissue analyzed for `"SampleOrigin"` `brain`.

    """

    gray_matter = "gray matter"
    white_matter = "white matter"
    csf = "csf"
    meninges = "meninges"
    macrovascular = "macrovascular"
    microvascular = "microvascular"


class Type(Enum):
    """
        Short identifier of the mask.
    The value `"Brain"` refers to a brain mask.
    The value `"Lesion"` refers to a lesion mask.
    The value `"Face"` refers to a face mask.
    The value `"ROI"` refers to a region of interest mask.

    """

    Brain = "Brain"
    Lesion = "Lesion"
    Face = "Face"
    ROI = "ROI"


class _CoordUnits(Enum):
    m = "m"
    mm = "mm"
    cm = "cm"
    n_a = "n/a"


class _EEGCoordSys(Enum):
    CapTrak = "CapTrak"
    EEGLAB = "EEGLAB"
    EEGLAB_HJ = "EEGLAB-HJ"
    Other = "Other"


class _GeneticLevelEnum(Enum):
    Genetic = "Genetic"
    Genomic = "Genomic"
    Epigenomic = "Epigenomic"
    Transcriptomic = "Transcriptomic"
    Metabolomic = "Metabolomic"
    Proteomic = "Proteomic"


class _MEGCoordSys(Enum):
    CTF = "CTF"
    ElektaNeuromag = "ElektaNeuromag"
    field_4DBti = "4DBti"
    KitYokogawa = "KitYokogawa"
    ChietiItab = "ChietiItab"
    Other = "Other"


class _StandardTemplateCoordSys(Enum):
    ICBM452AirSpace = "ICBM452AirSpace"
    ICBM452Warp5Space = "ICBM452Warp5Space"
    IXI549Space = "IXI549Space"
    fsaverage = "fsaverage"
    fsaverageSym = "fsaverageSym"
    fsLR = "fsLR"
    MNIColin27 = "MNIColin27"
    MNI152Lin = "MNI152Lin"
    MNI152NLin2009aSym = "MNI152NLin2009aSym"
    MNI152NLin2009bSym = "MNI152NLin2009bSym"
    MNI152NLin2009cSym = "MNI152NLin2009cSym"
    MNI152NLin2009aAsym = "MNI152NLin2009aAsym"
    MNI152NLin2009bAsym = "MNI152NLin2009bAsym"
    MNI152NLin2009cAsym = "MNI152NLin2009cAsym"
    MNI152NLin6Sym = "MNI152NLin6Sym"
    MNI152NLin6ASym = "MNI152NLin6ASym"
    MNI305 = "MNI305"
    NIHPD = "NIHPD"
    OASIS30AntsOASISAnts = "OASIS30AntsOASISAnts"
    OASIS30Atropos = "OASIS30Atropos"
    Talairach = "Talairach"
    UNCInfant = "UNCInfant"


class _StandardTemplateDeprecatedCoordSys(Enum):
    fsaverage3 = "fsaverage3"
    fsaverage4 = "fsaverage4"
    fsaverage5 = "fsaverage5"
    fsaverage6 = "fsaverage6"
    fsaveragesym = "fsaveragesym"
    UNCInfant0V21 = "UNCInfant0V21"
    UNCInfant1V21 = "UNCInfant1V21"
    UNCInfant2V21 = "UNCInfant2V21"
    UNCInfant0V22 = "UNCInfant0V22"
    UNCInfant1V22 = "UNCInfant1V22"
    UNCInfant2V22 = "UNCInfant2V22"
    UNCInfant0V23 = "UNCInfant0V23"
    UNCInfant1V23 = "UNCInfant1V23"
    UNCInfant2V23 = "UNCInfant2V23"


class _IEEGCoordSys(Enum):
    Pixels = "Pixels"
    ACPC = "ACPC"
    Other = "Other"


class IEEGCoordinateUnits(Enum):
    """
        Units of the `*_electrodes.tsv`.
    MUST be `"pixels"` if `iEEGCoordinateSystem` is `Pixels`.

    """

    m = "m"
    mm = "mm"
    cm = "cm"
    pixels = "pixels"
    n_a = "n/a"


class BidsMetadata(BaseModel):
    """
    This schema contains definitions for all metadata fields (fields which may  appear in sidecar JSON files) currently supported in BIDS.

    """

    Acknowledgements: Optional[str] = Field(
        None,
        description=(
            "Text acknowledging contributions of individuals or institutions"
            " beyond\nthose listed in Authors or Funding.\n"
        ),
    )
    AcquisitionDuration: Optional[PositiveFloat] = Field(
        None,
        description=(
            "Duration (in seconds) of volume acquisition.\nCorresponds to DICOM Tag"
            " 0018, 9073 `Acquisition Duration`.\nThis field is mutually exclusive with"
            ' `"RepetitionTime"`.\n'
        ),
    )
    AcquisitionMode: Optional[str] = Field(
        None,
        description=(
            'Type of acquisition of the PET data (for example, `"list mode"`).\n'
        ),
    )
    AcquisitionVoxelSize: Optional[List[AcquisitionVoxelSizeItem]] = Field(
        None,
        description=(
            "An array of numbers with a length of 3, in millimeters.\nThis parameter"
            " denotes the original acquisition voxel size,\nexcluding any inter-slice"
            " gaps and before any interpolation or resampling\nwithin reconstruction or"
            " image processing.\nAny point spread function effects, for example due to"
            " T2-blurring,\nthat would decrease the effective resolution are not"
            " considered here.\n"
        ),
        max_items=3,
        min_items=3,
    )
    Anaesthesia: Optional[str] = Field(
        None, description="Details of anaesthesia used, if any.\n"
    )
    AnalyticalApproach: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            'Methodology or methodologies used to analyse the `"GeneticLevel"`.\nValues'
            " MUST be taken from the\n[database of Genotypes and"
            " Phenotypes\n(dbGaP)](https://www.ncbi.nlm.nih.gov/gap/advanced)\nunder"
            " /Study/Molecular Data Type (for example, SNP Genotypes (Array)"
            " or\nMethylation (CpG).\n"
        ),
    )
    AnatomicalLandmarkCoordinateSystem: Optional[Union[Any, Any, Any, Any]] = Field(
        None,
        description=(
            "Defines the coordinate system for the anatomical landmarks.\nSee [Appendix"
            " VIII](/99-appendices/08-coordinate-systems.html)\nfor a list of"
            ' restricted keywords for coordinate systems.\nIf `"Other"`, provide'
            " definition of the coordinate system"
            ' in\n`"AnatomicalLandmarkCoordinateSystemDescription"`.\n'
        ),
    )
    AnatomicalLandmarkCoordinateSystemDescription: Optional[str] = Field(
        None,
        description=(
            "Free-form text description of the coordinate system.\nMay also include a"
            " link to a documentation page or paper describing the\nsystem in greater"
            " detail.\n"
        ),
    )
    AnatomicalLandmarkCoordinateUnits: Optional[
        AnatomicalLandmarkCoordinateUnits
    ] = Field(
        None,
        description=(
            'Units of the coordinates of `"AnatomicalLandmarkCoordinateSystem"`.\n'
        ),
    )
    AnatomicalLandmarkCoordinates: Optional[Dict[str, List[float]]] = Field(
        None,
        description=(
            "Key:value pairs of the labels and 3-D digitized locations of anatomical"
            " landmarks,\ninterpreted following the"
            ' `"AnatomicalLandmarkCoordinateSystem"`\n(for example, `{"NAS":'
            ' [12.7,21.3,13.9], "LPA": [5.2,11.3,9.6],\n"RPA": [20.2,11.3,9.1]}`.\nEach'
            " array MUST contain three numeric values corresponding to x, y, and"
            " z\naxis of the coordinate system in that exact order.\n"
        ),
    )
    AnatomicalLandmarkCoordinates__mri: Optional[Dict[str, List[float]]] = Field(
        None,
        description=(
            "Key:value pairs of any number of additional anatomical landmarks and"
            " their\ncoordinates in voxel units (where first voxel has index"
            ' 0,0,0)\nrelative to the associated anatomical MRI\n(for example, `{"AC":'
            ' [127,119,149], "PC": [128,93,141],\n"IH": [131,114,206]}`, or `{"NAS":'
            ' [127,213,139], "LPA": [52,113,96],\n"RPA": [202,113,91]}`).\nEach array'
            " MUST contain three numeric values corresponding to x, y, and z\naxis of"
            " the coordinate system in that exact order.\n"
        ),
    )
    ArterialSpinLabelingType: Optional[ArterialSpinLabelingType] = Field(
        None, description="The arterial spin labeling type.\n"
    )
    AssociatedEmptyRoom: Optional[Union[List[str], str]] = Field(
        None,
        description=(
            "Relative path in BIDS folder structure to empty-room file associated"
            " with\nthe subject's MEG recording.\nThe path needs to use forward"
            " slashes instead of backward slashes\n(for"
            ' example,\n"sub-emptyroom/ses-/meg/sub-emptyroom_ses-_task-noise_run-_meg.ds").\n'
        ),
    )
    Atlas: Optional[str] = Field(
        None, description="Which atlas (if any) was used to generate the mask.\n"
    )
    AttenuationCorrection: Optional[str] = Field(
        None,
        description="Short description of the attenuation correction method used.\n",
    )
    AttenuationCorrectionMethodReference: Optional[str] = Field(
        None,
        description="Reference paper for the attenuation correction method used.\n",
    )
    Authors: Optional[List[str]] = Field(
        None,
        description=(
            "List of individuals who contributed to the creation/curation of the"
            " dataset.\n"
        ),
    )
    B0FieldIdentifier: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "The presence of this key states that this particular 3D or 4D image MAY"
            ' be\nused for fieldmap estimation purposes.\nEach `"B0FieldIdentifier"`'
            " MUST be a unique string within one participant's tree,\nshared only by"
            " the images meant to be used as inputs for the estimation of a\nparticular"
            " instance of the *B<sub>0</sub> field* estimation.\nIt is RECOMMENDED to"
            " derive this identifier from DICOM Tags, for example,\nDICOM tag 0018,"
            " 1030 `Protocol Name`, or DICOM tag 0018, 0024 `Sequence Name`\nwhen the"
            " former is not defined (for example, in GE devices.)\n"
        ),
    )
    B0FieldSource: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            'At least one existing `"B0FieldIdentifier"` defined by images in'
            " the\nparticipant's tree.\nThis field states the *B<sub>0</sub> field*"
            ' estimation designated by the\n`"B0FieldIdentifier"` that may be used to'
            " correct the dataset for distortions\ncaused by B<sub>0</sub>"
            ' inhomogeneities.\n`"B0FieldSource"` and `"B0FieldIdentifier"` MAY both be'
            " present for images that\nare used to estimate their own B<sub>0</sub>"
            ' field, for example, in "pepolar"\nacquisitions.\n'
        ),
    )
    BIDSVersion: Optional[str] = Field(
        None, description="The version of the BIDS standard that was used.\n"
    )
    BackgroundSuppression: Optional[bool] = Field(
        None, description="Boolean indicating if background suppression is used.\n"
    )
    BackgroundSuppressionNumberPulses: Optional[confloat(ge=0.0)] = Field(
        None,
        description=(
            "The number of background suppression pulses used.\nNote that this excludes"
            " any effect of background suppression pulses applied\nbefore the"
            " labeling.\n"
        ),
    )
    BackgroundSuppressionPulseTime: Optional[List[confloat(ge=0.0)]] = Field(
        None,
        description=(
            "Array of numbers containing timing, in seconds,\nof the background"
            " suppression pulses with respect to the start of the\nlabeling.\nIn case"
            " of multi-PLD with different background suppression pulse times,\nonly the"
            " pulse time of the first PLD should be defined.\n"
        ),
    )
    BasedOn: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "List of files in a file collection to generate the map.\nFieldmaps are"
            " also listed, if involved in the processing.\n"
        ),
    )
    BloodDensity: Optional[float] = Field(
        None,
        description=(
            'Measured blood density. Unit of blood density should be in `"g/mL"`.\n'
        ),
    )
    BodyPart: Optional[str] = Field(
        None, description="Body part of the organ / body region scanned.\n"
    )
    BodyPartDetails: Optional[str] = Field(
        None,
        description=(
            'Additional details about body part or location (for example: `"corpus'
            ' callosum"`).\n'
        ),
    )
    BodyPartDetailsOntology: Optional[AnyUrl] = Field(
        None,
        description=(
            "[URI](/02-common-principles.html#uniform-resource-indicator) of ontology"
            " used for\nBodyPartDetails (for example:"
            ' `"https://www.ebi.ac.uk/ols/ontologies/uberon"`).\n'
        ),
    )
    BolusCutOffDelayTime: Optional[
        Union[confloat(ge=0.0), List[confloat(ge=0.0)]]
    ] = Field(
        None,
        description=(
            "Duration between the end of the labeling and the start of the bolus"
            " cut-off\nsaturation pulse(s), in seconds.\nThis can be a number or array"
            " of numbers, of which the values must be\nnon-negative and monotonically"
            " increasing, depending on the number of bolus\ncut-off saturation"
            " pulses.\nFor Q2TIPS, only the values for the first and last bolus cut-off"
            " saturation\npulses are provided.\nBased on DICOM Tag 0018, 925F `ASL"
            " Bolus Cut-off Delay Time`.\n"
        ),
    )
    BolusCutOffFlag: Optional[bool] = Field(
        None,
        description=(
            "Boolean indicating if a bolus cut-off technique is used.\nCorresponds to"
            " DICOM Tag 0018, 925C `ASL Bolus Cut-off Flag`.\n"
        ),
    )
    BolusCutOffTechnique: Optional[str] = Field(
        None,
        description=(
            'Name of the technique used, for example `"Q2TIPS"`, `"QUIPSS"`,'
            ' `"QUIPSSII"`.\nCorresponds to DICOM Tag 0018, 925E `ASL Bolus Cut-off'
            " Technique`.\n"
        ),
    )
    BrainLocation: Optional[str] = Field(
        None,
        description=(
            'Refers to the location in space of the `"TissueOrigin"`.\nValues may be an'
            " MNI coordinate,\na label taken from the\n[Allen Brain"
            " Atlas](https://atlas.brain-map.org/atlas?atlas=265297125&plate=\\\n112360888&structure=4392&x=40348.15104166667&y=46928.75&zoom=-7&resolution=\\\n206.60&z=3),\nor"
            " layer to refer to layer-specific gene expression,\nwhich can also tie up"
            " with laminar fMRI.\n"
        ),
    )
    CASLType: Optional[CASLType] = Field(
        None, description="Describes if a separate coil is used for labeling.\n"
    )
    CapManufacturer: Optional[str] = Field(
        None, description='Name of the cap manufacturer (for example, `"EasyCap"`).\n'
    )
    CapManufacturersModelName: Optional[str] = Field(
        None,
        description=(
            "Manufacturer's designation of the EEG cap model\n(for example, `\"actiCAP"
            ' 64 Ch Standard-2"`).\n'
        ),
    )
    CellType: Optional[str] = Field(
        None,
        description=(
            "Describes the type of cell analyzed.\nValues SHOULD come from the\n[cell"
            " ontology](http://obofoundry.org/ontology/cl.html).\n"
        ),
    )
    ChunkTransformationMatrix: Optional[
        Union[List[ChunkTransformationMatrixItem], List[ChunkTransformationMatrixItem1]]
    ] = Field(
        None,
        description=(
            "3x3 or 4x4 affine transformation matrix describing spatial chunk"
            " transformation,\nfor 2D and 3D respectively (for examples: `[[2, 0, 0],"
            " [0, 3, 0], [0, 0, 1]]`\nin 2D for 2x and 3x scaling along the first and"
            " second axis respectively; or\n`[[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0],"
            " [0, 0, 0, 1]]` in 3D for 2x and 3x\nscaling along the second and third"
            " axis respectively).\nNote that non-spatial dimensions like time and"
            " channel are not included in the\ntransformation matrix.\n"
        ),
    )
    ChunkTransformationMatrixAxis: Optional[List[str]] = Field(
        None,
        description=(
            'Describe the axis of the ChunkTransformationMatrix\n(for examples: `["X",'
            ' "Y"]` or `["Z", "Y", "X"]`).\n'
        ),
        max_items=3,
        min_items=2,
    )
    Code: Optional[AnyUrl] = Field(
        None,
        description=(
            "[URI](/02-common-principles.html#uniform-resource-indicator)\nof the code"
            " used to present the stimuli.\nPersistent identifiers such as DOIs are"
            " preferred.\nIf multiple versions of code may be hosted at the same"
            " location,\nrevision-specific URIs are recommended.\n"
        ),
    )
    CogAtlasID: Optional[AnyUrl] = Field(
        None,
        description=(
            "[URI](/02-common-principles.html#uniform-resource-indicator)\nof the"
            " corresponding [Cognitive Atlas](https://www.cognitiveatlas.org/)\nTask"
            " term.\n"
        ),
    )
    CogPOID: Optional[AnyUrl] = Field(
        None,
        description=(
            "[URI](/02-common-principles.html#uniform-resource-indicator)\nof the"
            " corresponding [CogPO](http://www.cogpo.org/) term.\n"
        ),
    )
    CoilCombinationMethod: Optional[str] = Field(
        None,
        description=(
            "Almost all fMRI studies using phased-array coils use"
            " root-sum-of-squares\n(rSOS) combination, but other methods exist.\nThe"
            " image reconstruction is changed by the coil combination method\n(as for"
            " the matrix coil mode above),\nso anything non-standard should be"
            " reported.\n"
        ),
    )
    Columns: Optional[List[str]] = Field(
        None, description="Names of columns in file.\n"
    )
    ContinuousHeadLocalization: Optional[bool] = Field(
        None,
        description=(
            "`true` or `false` value indicating whether continuous head"
            " localisation\nwas performed.\n"
        ),
    )
    ContrastBolusIngredient: Optional[ContrastBolusIngredient] = Field(
        None,
        description=(
            "Active ingredient of agent.\nCorresponds to DICOM Tag 0018, 1048"
            " `Contrast/Bolus Ingredient`.\n"
        ),
    )
    DCOffsetCorrection: Optional[str] = Field(
        None,
        description=(
            "A description of the method (if any) used to correct for a DC offset.\nIf"
            " the method used was subtracting the mean value for each channel,\nuse"
            ' "mean".\n'
        ),
    )
    DatasetDOI: Optional[AnyUrl] = Field(
        None,
        description=(
            "The Digital Object Identifier of the dataset (not the corresponding"
            " paper).\nDOIs SHOULD be expressed as a"
            " valid\n[URI](/02-common-principles.html#uniform-resource-indicator);\nbare"
            " DOIs such as `10.0.2.3/dfjj.10`"
            " are\n[DEPRECATED](/02-common-principles.html#definitions).\n"
        ),
    )
    DatasetType: Optional[DatasetType] = Field(
        None,
        description=(
            "The interpretation of the dataset.\nFor backwards compatibility, the"
            ' default value is `"raw"`.\n'
        ),
    )
    DecayCorrectionFactor: Optional[List[float]] = Field(
        None, description="Decay correction factor for each frame.\n"
    )
    DelayAfterTrigger: Optional[float] = Field(
        None,
        description=(
            "Duration (in seconds) from trigger delivery to scan onset.\nThis delay is"
            " commonly caused by adjustments and loading times.\nThis specification is"
            ' entirely independent of\n`"NumberOfVolumesDiscardedByScanner"` or'
            ' `"NumberOfVolumesDiscardedByUser"`,\nas the delay precedes the'
            " acquisition.\n"
        ),
    )
    DelayTime: Optional[float] = Field(
        None,
        description=(
            "User specified time (in seconds) to delay the acquisition of data for"
            " the\nfollowing volume.\nIf the field is not present it is assumed to be"
            " set to zero.\nCorresponds to Siemens CSA header field"
            " `lDelayTimeInTR`.\nThis field is REQUIRED for sparse sequences using the"
            ' `"RepetitionTime"` field\nthat do not have the `"SliceTiming"` field set'
            ' to allowed for accurate\ncalculation of "acquisition time".\nThis field'
            ' is mutually exclusive with `"VolumeTiming"`.\n'
        ),
    )
    Density: Optional[Union[str, Dict[str, str]]] = Field(
        None,
        description=(
            "Specifies the interpretation of the density keyword.\nIf an object is"
            " used, then the keys should be values for the ``den`` entity\nand values"
            " should be descriptions of those ``den`` values.\n"
        ),
    )
    Derivative: Optional[bool] = Field(
        None,
        description=(
            "Indicates that values in the corresponding column are transformations of"
            " values\nfrom other columns (for example a summary score based on a subset"
            " of items in a\nquestionnaire).\n"
        ),
    )
    Description: Optional[str] = Field(
        None, description="Free-form natural language description.\n"
    )
    DeviceSerialNumber: Optional[str] = Field(
        None,
        description=(
            "The serial number of the equipment that produced the measurements.\nA"
            " pseudonym can also be used to prevent the equipment from"
            " being\nidentifiable, so long as each pseudonym is unique within the"
            " dataset.\n"
        ),
    )
    DewarPosition: Optional[str] = Field(
        None,
        description=(
            'Position of the dewar during the MEG scan:\n`"upright"`, `"supine"` or'
            ' `"degrees"` of angle from vertical:\nfor example on CTF systems,'
            ' `"upright=15°, supine=90°"`.\n'
        ),
    )
    DigitizedHeadPoints: Optional[bool] = Field(
        None,
        description=(
            "`true` or `false` value indicating whether head points outlining"
            " the\nscalp/face surface are contained within this recording.\n"
        ),
    )
    DigitizedHeadPointsCoordinateSystem: Optional[Union[Any, Any, Any, Any]] = Field(
        None,
        description=(
            "Defines the coordinate system for the digitized head"
            " points.\nSee\n[Appendix"
            " VIII](/99-appendices/08-coordinate-systems.html)\nfor a list of"
            ' restricted keywords for coordinate systems.\nIf `"Other"`, provide'
            " definition of the coordinate system"
            ' in\n`"DigitizedHeadPointsCoordinateSystemDescription"`.\n'
        ),
    )
    DigitizedHeadPointsCoordinateSystemDescription: Optional[str] = Field(
        None,
        description=(
            "Free-form text description of the coordinate system.\nMay also include a"
            " link to a documentation page or paper describing the\nsystem in greater"
            " detail.\n"
        ),
    )
    DigitizedHeadPointsCoordinateUnits: Optional[
        DigitizedHeadPointsCoordinateUnits
    ] = Field(
        None,
        description=(
            'Units of the coordinates of `"DigitizedHeadPointsCoordinateSystem"`.\n'
        ),
    )
    DigitizedLandmarks: Optional[bool] = Field(
        None,
        description=(
            "`true` or `false` value indicating whether anatomical landmark"
            " points\n(fiducials) are contained within this recording.\n"
        ),
    )
    DispersionConstant: Optional[float] = Field(
        None,
        description=(
            "External dispersion time constant resulting from tubing in default"
            " unit\nseconds.\n"
        ),
    )
    DispersionCorrected: Optional[bool] = Field(
        None,
        description=(
            "Boolean flag specifying whether the blood data have been"
            " dispersion-corrected.\nNOTE: not customary for manual samples, and hence"
            " should be set to `false`.\n"
        ),
    )
    DoseCalibrationFactor: Optional[float] = Field(
        None,
        description=(
            "Multiplication factor used to transform raw data (in counts/sec) to"
            " meaningful unit (Bq/ml).\nCorresponds to DICOM Tag 0054, 1322 `Dose"
            " Calibration Factor`.\n"
        ),
    )
    DwellTime: Optional[float] = Field(
        None,
        description=(
            "Actual dwell time (in seconds) of the receiver per point in the"
            " readout\ndirection, including any oversampling.\nFor Siemens, this"
            " corresponds to DICOM field 0019, 1018 (in ns).\nThis value is necessary"
            " for the optional readout distortion correction of\nanatomicals in the HCP"
            " Pipelines.\nIt also usefully provides a handle on the readout"
            " bandwidth,\nwhich isn't captured in the other metadata tags.\nNot to be"
            ' confused with `"EffectiveEchoSpacing"`, and the frequent mislabeling\nof'
            " echo spacing (which is spacing in the phase encoding direction)"
            ' as\n"dwell time" (which is spacing in the readout direction).\n'
        ),
    )
    ECGChannelCount: Optional[conint(ge=0)] = Field(
        None, description="Number of ECG channels.\n"
    )
    ECOGChannelCount: Optional[conint(ge=0)] = Field(
        None, description="Number of ECoG channels.\n"
    )
    EEGChannelCount: Optional[conint(ge=0)] = Field(
        None,
        description=(
            "Number of EEG channels recorded simultaneously (for example, `21`).\n"
        ),
    )
    EEGCoordinateSystem: Optional[Union[Any, Any, Any, Any]] = Field(
        None,
        description=(
            "Defines the coordinate system for the EEG sensors.\n\nSee\n[Appendix"
            " VIII](/99-appendices/08-coordinate-systems.html)\nfor a list of"
            ' restricted keywords for coordinate systems.\nIf `"Other"`, provide'
            " definition of the coordinate system"
            " in\n`EEGCoordinateSystemDescription`.\n"
        ),
    )
    EEGCoordinateSystemDescription: Optional[str] = Field(
        None,
        description=(
            "Free-form text description of the coordinate system.\nMay also include a"
            " link to a documentation page or paper describing the\nsystem in greater"
            " detail.\n"
        ),
    )
    EEGCoordinateUnits: Optional[EEGCoordinateUnits] = Field(
        None, description="Units of the coordinates of `EEGCoordinateSystem`.\n"
    )
    EEGGround: Optional[str] = Field(
        None,
        description=(
            "Description of the location of the ground electrode\n(for example,"
            ' `"placed on right mastoid (M2)"`).\n'
        ),
    )
    EEGPlacementScheme: Optional[str] = Field(
        None,
        description=(
            "Placement scheme of EEG electrodes.\nEither the name of a standardized"
            ' placement system (for example, `"10-20"`)\nor a list of standardized'
            ' electrode names (for example, `["Cz", "Pz"]`).\n'
        ),
    )
    EEGReference: Optional[str] = Field(
        None,
        description=(
            "General description of the reference scheme used and (when applicable)"
            " of\nlocation of the reference electrode in the raw recordings\n(for"
            ' example, `"left mastoid"`, `"Cz"`, `"CMS"`).\nIf different channels have'
            " a different reference,\nthis field should have a general description and"
            " the channel specific\nreference should be defined in the `channels.tsv`"
            " file.\n"
        ),
    )
    EMGChannelCount: Optional[conint(ge=0)] = Field(
        None, description="Number of EMG channels.\n"
    )
    EOGChannelCount: Optional[conint(ge=0)] = Field(
        None, description="Number of EOG channels.\n"
    )
    EchoTime: Optional[Union[PositiveFloat, List[PositiveFloat]]] = Field(
        None,
        description=(
            "The echo time (TE) for the acquisition, specified in seconds.\nCorresponds"
            " to DICOM Tag 0018, 0081 `Echo Time`\n(please note that the DICOM term is"
            " in milliseconds not seconds).\nThe data type number may apply to files"
            " from any MRI modality concerned with\na single value for this field, or"
            " to the files in a\n[file"
            " collection](/99-appendices/10-file-collections.html)\nwhere the value of"
            " this field is iterated using the\n[echo"
            " entity](/99-appendices/09-entities.html#echo).\nThe data type array"
            " provides a value for each volume in a 4D dataset and\nshould only be used"
            " when the volume timing is critical for interpretation\nof the data, such"
            " as in\n[ASL](/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#\\\narterial-spin-labeling-perfusion-data)\nor"
            " variable echo time fMRI sequences.\n"
        ),
    )
    EchoTime1: Optional[PositiveFloat] = Field(
        None,
        description="The time (in seconds) when the first (shorter) echo occurs.\n",
    )
    EchoTime2: Optional[PositiveFloat] = Field(
        None,
        description="The time (in seconds) when the second (longer) echo occurs.\n",
    )
    EchoTime__fmap: Optional[PositiveFloat] = Field(
        None,
        description=(
            "The time (in seconds) when the echo corresponding to this map was"
            " acquired.\n"
        ),
    )
    EffectiveEchoSpacing: Optional[PositiveFloat] = Field(
        None,
        description=(
            'The "effective" sampling interval, specified in seconds,\nbetween lines in'
            " the phase-encoding direction,\ndefined based on the size of the"
            " reconstructed image in the phase direction.\nIt is frequently, but"
            ' incorrectly, referred to as "dwell time"\n(see the `"DwellTime"`'
            " parameter for actual dwell time).\nIt is required for unwarping"
            " distortions using field maps.\nNote that beyond just in-plane"
            " acceleration,\na variety of other manipulations to the phase encoding"
            " need to be accounted\nfor properly, including partial fourier, phase"
            " oversampling,\nphase resolution, phase field-of-view and interpolation.\n"
        ),
    )
    ElectricalStimulation: Optional[bool] = Field(
        None,
        description=(
            "Boolean field to specify if electrical stimulation was done during"
            " the\nrecording (options are `true` or `false`). Parameters for"
            " event-like\nstimulation should be specified in the `events.tsv` file.\n"
        ),
    )
    ElectricalStimulationParameters: Optional[str] = Field(
        None,
        description=(
            "Free form description of stimulation parameters, such as frequency or"
            " shape.\nSpecific onsets can be specified in the events.tsv"
            " file.\nSpecific shapes can be described here in freeform text.\n"
        ),
    )
    ElectrodeManufacturer: Optional[str] = Field(
        None,
        description=(
            "Can be used if all electrodes are of the same manufacturer\n(for example,"
            ' `"AD-TECH"`, `"DIXI"`).\nIf electrodes of different manufacturers are'
            " used,\nplease use the corresponding table in the `_electrodes.tsv`"
            " file.\n"
        ),
    )
    ElectrodeManufacturersModelName: Optional[str] = Field(
        None,
        description=(
            "If different electrode types are used,\nplease use the corresponding table"
            " in the `_electrodes.tsv` file.\n"
        ),
    )
    EpochLength: Optional[confloat(ge=0.0)] = Field(
        None,
        description=(
            "Duration of individual epochs in seconds (for example, `1`)\nin case of"
            " epoched data.\nIf recording was continuous or discontinuous, leave out"
            " the field.\n"
        ),
    )
    EstimationAlgorithm: Optional[str] = Field(
        None,
        description=(
            'Type of algorithm used to perform fitting\n(for example, `"linear"`,'
            ' `"non-linear"`, `"LM"` and such).\n'
        ),
    )
    EstimationReference: Optional[str] = Field(
        None,
        description=(
            "Reference to the study/studies on which the implementation is based.\n"
        ),
    )
    EthicsApprovals: Optional[List[str]] = Field(
        None,
        description=(
            "List of ethics committee approvals of the research protocols"
            " and/or\nprotocol identifiers.\n"
        ),
    )
    FiducialsCoordinateSystem: Optional[Union[Any, Any, Any, Any]] = Field(
        None,
        description=(
            "Defines the coordinate system for the fiducials.\nPreferably the same as"
            ' the `"EEGCoordinateSystem"`.\nSee\n[Appendix'
            " VIII](/99-appendices/08-coordinate-systems.html)\nfor a list of"
            ' restricted keywords for coordinate systems.\nIf `"Other"`, provide'
            " definition of the coordinate system"
            ' in\n`"FiducialsCoordinateSystemDescription"`.\n'
        ),
    )
    FiducialsCoordinateSystemDescription: Optional[str] = Field(
        None,
        description=(
            "Free-form text description of the coordinate system.\nMay also include a"
            " link to a documentation page or paper describing the\nsystem in greater"
            " detail.\n"
        ),
    )
    FiducialsCoordinateUnits: Optional[FiducialsCoordinateUnits] = Field(
        None,
        description=(
            "Units in which the coordinates that are  listed in the"
            ' field\n`"FiducialsCoordinateSystem"` are represented.\n'
        ),
    )
    FiducialsCoordinates: Optional[Dict[str, List[float]]] = Field(
        None,
        description=(
            "Key:value pairs of the labels and 3-D digitized position of"
            " anatomical\nlandmarks, interpreted following the"
            ' `"FiducialsCoordinateSystem"`\n(for example, `{"NAS": [12.7,21.3,13.9],'
            ' "LPA": [5.2,11.3,9.6],\n"RPA": [20.2,11.3,9.1]}`).\nEach array MUST'
            " contain three numeric values corresponding to x, y, and z\naxis of the"
            " coordinate system in that exact order.\n"
        ),
    )
    FiducialsDescription: Optional[str] = Field(
        None,
        description=(
            "Free-form text description of how the fiducials such as vitamin-E"
            " capsules\nwere placed relative to anatomical landmarks,\nand how the"
            ' position of the fiducials were measured\n(for example, `"both with'
            ' Polhemus and with T1w MRI"`).\n'
        ),
    )
    FlipAngle: Optional[
        Union[confloat(le=360.0, gt=0.0), List[confloat(le=360.0, gt=0.0)]]
    ] = Field(
        None,
        description=(
            "Flip angle (FA) for the acquisition, specified in degrees.\nCorresponds"
            " to: DICOM Tag 0018, 1314 `Flip Angle`.\nThe data type number may apply to"
            " files from any MRI modality concerned with\na single value for this"
            " field, or to the files in a\n[file"
            " collection](/99-appendices/10-file-collections.html)\nwhere the value of"
            " this field is iterated using the\n[flip"
            " entity](/99-appendices/09-entities.html#flip).\nThe data type array"
            " provides a value for each volume in a 4D dataset and\nshould only be used"
            " when the volume timing is critical for interpretation of\nthe data, such"
            " as in\n[ASL](/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#\\\narterial-spin-labeling-perfusion-data)\nor"
            " variable flip angle fMRI sequences.\n"
        ),
    )
    FrameDuration: Optional[List[float]] = Field(
        None,
        description=(
            "Time duration of each frame in default unit seconds.\nThis corresponds to"
            " DICOM Tag 0018, 1242 `Actual Frame Duration` converted\nto seconds.\n"
        ),
    )
    FrameTimesStart: Optional[List[float]] = Field(
        None,
        description=(
            'Start times for all frames relative to `"TimeZero"` in default unit'
            " seconds.\n"
        ),
    )
    Funding: Optional[List[str]] = Field(
        None, description="List of sources of funding (grant numbers).\n"
    )
    GeneratedBy: Optional[List[GeneratedByItem]] = Field(
        None, description="Used to specify provenance of the dataset.\n", min_items=1
    )
    GeneticLevel: Optional[Union[Any, List[Any]]] = Field(
        None,
        description=(
            'Describes the level of analysis.\nValues MUST be one of `"Genetic"`,'
            ' `"Genomic"`, `"Epigenomic"`,\n`"Transcriptomic"`, `"Metabolomic"`, or'
            ' `"Proteomic"`.\n'
        ),
    )
    Genetics_Database: Optional[AnyUrl] = Field(
        None,
        alias="Genetics.Database",
        description=(
            "[URI](/02-common-principles.html#uniform-resource-indicator)\nof database"
            " where the dataset is hosted.\n"
        ),
    )
    Genetics_Dataset: Optional[AnyUrl] = Field(
        None,
        alias="Genetics.Dataset",
        description=(
            "[URI](/02-common-principles.html#uniform-resource-indicator)\nwhere data"
            " can be retrieved.\n"
        ),
    )
    Genetics_Descriptors: Optional[Union[str, List[str]]] = Field(
        None,
        alias="Genetics.Descriptors",
        description=(
            "List of relevant descriptors (for example, journal articles) for"
            " dataset\nusing a"
            " valid\n[URI](/02-common-principles.html#uniform-resource-indicator)\nwhen"
            " possible.\n"
        ),
    )
    Genetics: Optional[Genetics] = Field(
        None,
        description="An object containing information about the genetics descriptor.\n",
    )
    GradientSetType: Optional[str] = Field(
        None,
        description=(
            "It should be possible to infer the gradient coil from the scanner"
            " model.\nIf not, for example because of a custom upgrade or use of a"
            " gradient\ninsert set, then the specifications of the actual gradient coil"
            " should be\nreported independently.\n"
        ),
    )
    HED: Optional[Union[str, Dict[str, str]]] = Field(
        None,
        description=(
            "Hierarchical Event Descriptor (HED) information,\nsee: [Appendix"
            " III](/99-appendices/03-hed.html) for details.\n"
        ),
    )
    HEDVersion: Optional[str] = Field(
        None,
        description=(
            "If HED tags are used:\nThe version of the HED schema used to validate HED"
            " tags for study.\n"
        ),
    )
    Haematocrit: Optional[float] = Field(
        None,
        description=(
            "Measured haematocrit, meaning the volume of erythrocytes divided by"
            " the\nvolume of whole blood.\n"
        ),
    )
    HardcopyDeviceSoftwareVersion: Optional[str] = Field(
        None,
        description=(
            "Manufacturer's designation of the software of the device that created"
            " this\nHardcopy Image (the printer).\nCorresponds to DICOM Tag 0018, 101A"
            " `Hardcopy Device Software Version`.\n"
        ),
    )
    HardwareFilters: Optional[Union[Dict[str, Dict[str, Any]], HardwareFilter]] = Field(
        None,
        description=(
            'Object of temporal hardware filters applied, or `"n/a"` if the data is'
            " not\navailable. Each key:value pair in the JSON object is a name of the"
            " filter and\nan object in which its parameters are defined as key:value"
            ' pairs.\nFor example, `{"Highpass RC filter": {"Half amplitude cutoff'
            ' (Hz)":\n0.0159, "Roll-off": "6dB/Octave"}}`.\n'
        ),
    )
    HeadCircumference: Optional[PositiveFloat] = Field(
        None,
        description=(
            "Circumference of the participant's head, expressed in cm (for example,"
            " `58`).\n"
        ),
    )
    HeadCoilCoordinateSystem: Optional[Union[Any, Any, Any, Any]] = Field(
        None,
        description=(
            "Defines the coordinate system for the head coils.\nSee\n[Appendix"
            " VIII](/99-appendices/08-coordinate-systems.html)\nfor a list of"
            ' restricted keywords for coordinate systems.\nIf `"Other"`, provide'
            " definition of the coordinate system"
            " in\n`HeadCoilCoordinateSystemDescription`.\n"
        ),
    )
    HeadCoilCoordinateSystemDescription: Optional[str] = Field(
        None,
        description=(
            "Free-form text description of the coordinate system.\nMay also include a"
            " link to a documentation page or paper describing the system in greater"
            " detail.\n"
        ),
    )
    HeadCoilCoordinateUnits: Optional[HeadCoilCoordinateUnits] = Field(
        None, description="Units of the coordinates of `HeadCoilCoordinateSystem`.\n"
    )
    HeadCoilCoordinates: Optional[Dict[str, List[float]]] = Field(
        None,
        description=(
            "Key:value pairs describing head localization coil labels and"
            " their\ncoordinates, interpreted following the"
            ' `HeadCoilCoordinateSystem`\n(for example, `{"NAS": [12.7,21.3,13.9],'
            ' "LPA": [5.2,11.3,9.6],\n"RPA": [20.2,11.3,9.1]}`).\nNote that coils are'
            " not always placed at locations that have a known\nanatomical name (for"
            " example, for Elekta, Yokogawa systems); in that case\ngeneric labels can"
            ' be used\n(for example, `{"coil1": [12.2,21.3,12.3], "coil2":'
            ' [6.7,12.3,8.6],\n"coil3": [21.9,11.0,8.1]}`).\nEach array MUST contain'
            " three numeric values corresponding to x, y, and z\naxis of the coordinate"
            " system in that exact order.\n"
        ),
    )
    HeadCoilFrequency: Optional[Union[float, List[float]]] = Field(
        None,
        description=(
            "List of frequencies (in Hz) used by the head localisation coils\n('HLC' in"
            " CTF systems, 'HPI' in Elekta, 'COH' in BTi/4D)\nthat track the subject's"
            " head position in the MEG helmet\n(for example, `[293, 307, 314, 321]`).\n"
        ),
    )
    HowToAcknowledge: Optional[str] = Field(
        None,
        description=(
            "Text containing instructions on how researchers using this dataset"
            " should\nacknowledge the original authors.\nThis field can also be used to"
            " define a publication that should be cited in\npublications that use the"
            " dataset.\n"
        ),
    )
    ImageAcquisitionProtocol: Optional[str] = Field(
        None,
        description=(
            "Description of the image acquisition protocol"
            " or\n[URI](/02-common-principles.html#uniform-resource-indicator)\n(for"
            " example from [protocols.io](https://www.protocols.io/)).\n"
        ),
    )
    ImageDecayCorrected: Optional[bool] = Field(
        None,
        description=(
            "Boolean flag specifying whether the image data have been"
            " decay-corrected.\n"
        ),
    )
    ImageDecayCorrectionTime: Optional[float] = Field(
        None,
        description=(
            "Point in time from which the decay correction was applied with respect"
            ' to\n`"TimeZero"` in the default unit seconds.\n'
        ),
    )
    Immersion: Optional[str] = Field(
        None,
        description=(
            "Lens immersion medium. If the file format is OME-TIFF, the value MUST be"
            " consistent\nwith the `Immersion` OME metadata field.\n"
        ),
    )
    InfusionRadioactivity: Optional[float] = Field(
        None,
        description=(
            "Amount of radioactivity infused into the patient.\nThis value must be less"
            " than or equal to the total injected"
            ' radioactivity\n(`"InjectedRadioactivity"`).\nUnits should be the same as'
            ' `"InjectedRadioactivityUnits"`.\n'
        ),
    )
    InfusionSpeed: Optional[float] = Field(
        None, description="If given, infusion speed.\n"
    )
    InfusionSpeedUnits: Optional[str] = Field(
        None, description='Unit of infusion speed (for example, `"mL/s"`).\n'
    )
    InfusionStart: Optional[float] = Field(
        None,
        description=(
            'Time of start of infusion with respect to `"TimeZero"` in the default'
            " unit\nseconds.\n"
        ),
    )
    InjectedMass: Optional[Union[float, InjectedMas]] = Field(
        None,
        description=(
            "Total mass of radiolabeled compound injected into subject (for example,"
            ' `10`).\nThis can be derived as the ratio of the `"InjectedRadioactivity"`'
            ' and\n`"MolarRadioactivity"`.\n**For those tracers in which injected mass'
            ' is not available (for example FDG)\ncan be set to `"n/a"`)**.\n'
        ),
    )
    InjectedMassPerWeight: Optional[float] = Field(
        None, description="Injected mass per kilogram bodyweight.\n"
    )
    InjectedMassPerWeightUnits: Optional[str] = Field(
        None,
        description=(
            "Unit format of the injected mass per kilogram bodyweight\n(for example,"
            ' `"ug/kg"`).\n'
        ),
    )
    InjectedMassUnits: Optional[Union[str, InjectedMassUnit]] = Field(
        None,
        description=(
            'Unit format of the mass of compound injected (for example, `"ug"`'
            ' or\n`"umol"`).\n**Note this is not required for an FDG acquisition, since'
            ' it is not available,\nand SHOULD be set to `"n/a"`**.\n'
        ),
    )
    InjectedRadioactivity: Optional[float] = Field(
        None,
        description=(
            "Total amount of radioactivity injected into the patient (for example,"
            " `400`).\nFor bolus-infusion experiments, this value should be the sum of"
            " all injected\nradioactivity originating from both bolus and"
            " infusion.\nCorresponds to DICOM Tag 0018, 1074 `Radionuclide Total"
            " Dose`.\n"
        ),
    )
    InjectedRadioactivityUnits: Optional[str] = Field(
        None,
        description=(
            "Unit format of the specified injected radioactivity (for example,"
            ' `"MBq"`).\n'
        ),
    )
    InjectedVolume: Optional[float] = Field(
        None, description='Injected volume of the radiotracer in the unit `"mL"`.\n'
    )
    InjectionEnd: Optional[float] = Field(
        None,
        description=(
            'Time of end of injection with respect to `"TimeZero"` in the default'
            " unit\nseconds.\n"
        ),
    )
    InjectionStart: Optional[float] = Field(
        None,
        description=(
            'Time of start of injection with respect to `"TimeZero"` in the default'
            " unit\nseconds.\nThis corresponds to DICOM Tag 0018, 1042 `Contrast/Bolus"
            ' Start Time`\nconverted to seconds relative to `"TimeZero"`.\n'
        ),
    )
    InstitutionAddress: Optional[str] = Field(
        None,
        description=(
            "The address of the institution in charge of the equipment that produced"
            " the\nmeasurements.\n"
        ),
    )
    InstitutionName: Optional[str] = Field(
        None,
        description=(
            "The name of the institution in charge of the equipment that produced"
            " the\nmeasurements.\n"
        ),
    )
    InstitutionalDepartmentName: Optional[str] = Field(
        None,
        description=(
            "The department in the institution in charge of the equipment that"
            " produced\nthe measurements.\n"
        ),
    )
    Instructions: Optional[str] = Field(
        None,
        description=(
            "Text of the instructions given to participants before the recording.\n"
        ),
    )
    IntendedFor: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "The paths to files for which the associated file is intended to be"
            " used.\nContains one or more filenames with paths relative to the"
            " participant\nsubfolder.\nPaths need to use forward slashes instead of"
            " backward slashes,\nregardless of operating system.\n"
        ),
    )
    InversionTime: Optional[PositiveFloat] = Field(
        None,
        description=(
            "The inversion time (TI) for the acquisition, specified in"
            " seconds.\nInversion time is the time after the middle of inverting RF"
            " pulse to middle\nof excitation pulse to detect the amount of longitudinal"
            " magnetization.\nCorresponds to DICOM Tag 0018, 0082 `Inversion"
            " Time`\n(please note that the DICOM term is in milliseconds not"
            " seconds).\n"
        ),
    )
    LabelingDistance: Optional[float] = Field(
        None,
        description=(
            "Distance from the center of the imaging slab to the center of the"
            " labeling\nplane (`(P)CASL`) or the leading edge of the labeling slab"
            " (`PASL`),\nin millimeters.\nIf the labeling is performed inferior to the"
            " isocenter,\nthis number should be negative.\nBased on DICOM macro"
            " C.8.13.5.14.\n"
        ),
    )
    LabelingDuration: Optional[Union[confloat(ge=0.0), List[confloat(ge=0.0)]]] = Field(
        None,
        description=(
            "Total duration of the labeling pulse train, in seconds,\ncorresponding to"
            ' the temporal width of the labeling bolus for\n`"PCASL"` or `"CASL"`.\nIn'
            " case all control-label volumes (or deltam or CBF) have the"
            " same\n`LabelingDuration`, a scalar must be specified.\nIn case the"
            " control-label volumes (or deltam or cbf) have a"
            ' different\n`"LabelingDuration"`, an array of numbers must be'
            " specified,\nfor which any `m0scan` in the timeseries has a"
            ' `"LabelingDuration"` of zero.\nIn case an array of numbers is'
            " provided,\nits length should be equal to the number of volumes specified"
            " in\n`*_aslcontext.tsv`.\nCorresponds to DICOM Tag 0018, 9258 `ASL Pulse"
            " Train Duration`.\n"
        ),
    )
    LabelingEfficiency: Optional[PositiveFloat] = Field(
        None,
        description=(
            "Labeling efficiency, specified as a number between zero and one,\nonly if"
            " obtained externally (for example phase-contrast based).\n"
        ),
    )
    LabelingLocationDescription: Optional[str] = Field(
        None,
        description=(
            'Description of the location of the labeling plane (`"CASL"` or `"PCASL"`)'
            ' or\nthe labeling slab (`"PASL"`) that cannot be captured by'
            " fields\n`LabelingOrientation` or `LabelingDistance`.\nMay include a link"
            " to an anonymized screenshot of the planning of the\nlabeling slab/plane"
            " with respect to the imaging slab or slices\n`*_asllabeling.jpg`.\nBased"
            " on DICOM macro C.8.13.5.14.\n"
        ),
    )
    LabelingOrientation: Optional[List[float]] = Field(
        None,
        description=(
            "Orientation of the labeling plane (`(P)CASL`) or slab (`PASL`).\nThe"
            " direction cosines of a normal vector perpendicular to the ASL"
            " labeling\nslab or plane with respect to the patient.\nCorresponds to"
            " DICOM Tag 0018, 9255 `ASL Slab Orientation`.\n"
        ),
    )
    LabelingPulseAverageB1: Optional[PositiveFloat] = Field(
        None,
        description=(
            "The average B1-field strength of the RF labeling pulses, in"
            ' microteslas.\nAs an alternative, `"LabelingPulseFlipAngle"` can be'
            " provided.\n"
        ),
    )
    LabelingPulseAverageGradient: Optional[PositiveFloat] = Field(
        None, description="The average labeling gradient, in milliteslas per meter.\n"
    )
    LabelingPulseDuration: Optional[PositiveFloat] = Field(
        None,
        description="Duration of the individual labeling pulses, in milliseconds.\n",
    )
    LabelingPulseFlipAngle: Optional[confloat(le=360.0, gt=0.0)] = Field(
        None,
        description=(
            "The flip angle of a single labeling pulse, in degrees,\nwhich can be given"
            ' as an alternative to `"LabelingPulseAverageB1"`.\n'
        ),
    )
    LabelingPulseInterval: Optional[PositiveFloat] = Field(
        None,
        description=(
            "Delay between the peaks of the individual labeling pulses, in"
            " milliseconds.\n"
        ),
    )
    LabelingPulseMaximumGradient: Optional[PositiveFloat] = Field(
        None,
        description=(
            "The maximum amplitude of the gradient switched on during the application"
            " of\nthe labeling RF pulse(s), in milliteslas per meter.\n"
        ),
    )
    LabelingSlabThickness: Optional[PositiveFloat] = Field(
        None,
        description=(
            "Thickness of the labeling slab in millimeters.\nFor non-selective FAIR a"
            " zero is entered.\nCorresponds to DICOM Tag 0018, 9254 `ASL Slab"
            " Thickness`.\n"
        ),
    )
    Levels: Optional[Dict[str, str]] = Field(
        None,
        description=(
            "For categorical variables: An object of possible values (keys) and"
            " their\ndescriptions (values).\n"
        ),
    )
    License: Optional[str] = Field(
        None,
        description=(
            "The license for the dataset.\nThe use of license name abbreviations is"
            " RECOMMENDED for specifying a license\n(see [Appendix"
            " II](/99-appendices/02-licenses.html)).\nThe corresponding full license"
            " text MAY be specified in an additional\n`LICENSE` file.\n"
        ),
    )
    LongName: Optional[str] = Field(
        None, description="Long (unabbreviated) name of the column.\n"
    )
    LookLocker: Optional[bool] = Field(
        None, description="Boolean indicating if a Look-Locker readout is used.\n"
    )
    M0Estimate: Optional[PositiveFloat] = Field(
        None,
        description=(
            "A single numerical whole-brain M0 value (referring to the M0 of"
            " blood),\nonly if obtained externally\n(for example retrieved from CSF in"
            " a separate measurement).\n"
        ),
    )
    M0Type: Optional[M0Type] = Field(
        None,
        description=(
            'Describes the presence of M0 information.\n`"Separate"` means that a'
            ' separate `*_m0scan.nii[.gz]` is present.\n`"Included"` means that an'
            " m0scan volume is contained within the"
            ' current\n`*_asl.nii[.gz]`.\n`"Estimate"` means that a single whole-brain'
            ' M0 value is provided.\n`"Absent"` means that no specific M0 information'
            " is present.\n"
        ),
    )
    MEGChannelCount: Optional[conint(ge=0)] = Field(
        None, description="Number of MEG channels (for example, `275`).\n"
    )
    MEGCoordinateSystem: Optional[Union[Any, Any, Any, Any]] = Field(
        None,
        description=(
            "Defines the coordinate system for the MEG sensors.\nSee [Appendix"
            " VIII](/99-appendices/08-coordinate-systems.html)\nfor a list of"
            ' restricted keywords for coordinate systems.\nIf `"Other"`, provide'
            " definition of the coordinate system"
            ' in\n`"MEGCoordinateSystemDescription"`.\n'
        ),
    )
    MEGCoordinateSystemDescription: Optional[str] = Field(
        None,
        description=(
            "Free-form text description of the coordinate system.\nMay also include a"
            " link to a documentation page or paper describing the\nsystem in greater"
            " detail.\n"
        ),
    )
    MEGCoordinateUnits: Optional[MEGCoordinateUnits] = Field(
        None, description='Units of the coordinates of `"MEGCoordinateSystem"`.\n'
    )
    MEGREFChannelCount: Optional[conint(ge=0)] = Field(
        None,
        description=(
            "Number of MEG reference channels (for example, `23`).\nFor systems without"
            " such channels (for example, Neuromag Vectorview),\n`MEGREFChannelCount`"
            " should be set to `0`.\n"
        ),
    )
    MRAcquisitionType: Optional[MRAcquisitionType] = Field(
        None,
        description=(
            "Type of sequence readout.\nCorresponds to DICOM Tag 0018, 0023 `MR"
            " Acquisition Type`.\n"
        ),
    )
    MRTransmitCoilSequence: Optional[str] = Field(
        None,
        description=(
            "This is a relevant field if a non-standard transmit coil is"
            " used.\nCorresponds to DICOM Tag 0018, 9049 `MR Transmit Coil Sequence`.\n"
        ),
    )
    MTNumberOfPulses: Optional[float] = Field(
        None,
        description=(
            "The number of magnetization transfer RF pulses applied before the"
            " readout.\n"
        ),
    )
    MTOffsetFrequency: Optional[float] = Field(
        None,
        description=(
            "The frequency offset of the magnetization transfer pulse with respect to"
            " the\ncentral H1 Larmor frequency in Hertz (Hz).\n"
        ),
    )
    MTPulseBandwidth: Optional[float] = Field(
        None,
        description=(
            "The excitation bandwidth of the magnetization transfer pulse in Hertz"
            " (Hz).\n"
        ),
    )
    MTPulseDuration: Optional[float] = Field(
        None,
        description="Duration of the magnetization transfer RF pulse in seconds.\n",
    )
    MTPulseShape: Optional[MTPulseShape] = Field(
        None,
        description=(
            "Shape of the magnetization transfer RF pulse waveform.\nThe value"
            ' `"GAUSSHANN"` refers to a Gaussian pulse with a Hanning window.\nThe'
            ' value `"SINCHANN"` refers to a sinc pulse with a Hanning window.\nThe'
            ' value `"SINCGAUSS"` refers to a sinc pulse with a Gaussian window.\n'
        ),
    )
    MTState: Optional[bool] = Field(
        None,
        description=(
            "Boolean stating whether the magnetization transfer pulse is"
            " applied.\nCorresponds to DICOM Tag 0018, 9020 `Magnetization Transfer`.\n"
        ),
    )
    MagneticFieldStrength: Optional[float] = Field(
        None,
        description=(
            "Nominal field strength of MR magnet in Tesla.\nCorresponds to DICOM Tag"
            " 0018, 0087 `Magnetic Field Strength`.\n"
        ),
    )
    Magnification: Optional[PositiveFloat] = Field(
        None,
        description=(
            "Lens magnification (for example: `40`). If the file format is"
            ' OME-TIFF,\nthe value MUST be consistent with the `"NominalMagnification"`'
            " OME metadata field.\n"
        ),
    )
    Manual: Optional[bool] = Field(
        None,
        description=(
            "Indicates if the segmentation was performed manually or via an"
            " automated\nprocess.\n"
        ),
    )
    Manufacturer: Optional[str] = Field(
        None,
        description="Manufacturer of the equipment that produced the measurements.\n",
    )
    ManufacturersModelName: Optional[str] = Field(
        None,
        description=(
            "Manufacturer's model name of the equipment that produced the"
            " measurements.\n"
        ),
    )
    MatrixCoilMode: Optional[str] = Field(
        None,
        description=(
            "(If used)\nA method for reducing the number of independent channels by"
            " combining in\nanalog the signals from multiple coil elements.\nThere are"
            " typically different default modes when using un-accelerated"
            ' or\naccelerated (for example, `"GRAPPA"`, `"SENSE"`) imaging.\n'
        ),
    )
    MaxMovement: Optional[float] = Field(
        None,
        description=(
            "Maximum head movement (in mm) detected during the recording,\nas measured"
            " by the head localisation coils (for example, `4.8`).\n"
        ),
    )
    MeasurementToolMetadata: Optional[MeasurementToolMetadata] = Field(
        None,
        description=(
            "A description of the measurement tool as a whole.\nContains two fields:"
            ' `"Description"` and `"TermURL"`.\n`"Description"` is a free text'
            ' description of the measurement tool.\n`"TermURL"` is a URL to an entity'
            " in an ontology corresponding to this tool.\n"
        ),
    )
    MetaboliteAvail: Optional[bool] = Field(
        None,
        description=(
            "Boolean that specifies if metabolite measurements are available.\nIf"
            " `true`, the `metabolite_parent_fraction` column MUST be present in"
            " the\ncorresponding `*_blood.tsv` file.\n"
        ),
    )
    MetaboliteMethod: Optional[str] = Field(
        None, description="Method used to measure metabolites.\n"
    )
    MetaboliteRecoveryCorrectionApplied: Optional[bool] = Field(
        None,
        description=(
            "Metabolite recovery correction from the HPLC, for tracers where it"
            " changes\nwith time postinjection.\nIf `true`, the"
            " `hplc_recovery_fractions` column MUST be present in the\ncorresponding"
            " `*_blood.tsv` file.\n"
        ),
    )
    MiscChannelCount: Optional[conint(ge=0)] = Field(
        None,
        description="Number of miscellaneous analog channels for auxiliary signals.\n",
    )
    MixingTime: Optional[float] = Field(
        None,
        description=(
            "In the context of a stimulated- and spin-echo 3D EPI sequence for B1+"
            " mapping,\ncorresponds to the interval between spin- and stimulated-echo"
            " pulses.\nIn the context of a diffusion-weighted double spin-echo"
            " sequence,\ncorresponds to the interval between two successive diffusion"
            " sensitizing\ngradients, specified in seconds.\n"
        ),
    )
    ModeOfAdministration: Optional[str] = Field(
        None,
        description=(
            'Mode of administration of the injection\n(for example, `"bolus"`,'
            ' `"infusion"`, or `"bolus-infusion"`).\n'
        ),
    )
    MolarActivity: Optional[float] = Field(
        None,
        description=(
            "Molar activity of compound injected.\nCorresponds to DICOM Tag 0018, 1077"
            " `Radiopharmaceutical Specific Activity`.\n"
        ),
    )
    MolarActivityMeasTime: Optional[
        constr(regex=r"^(?:2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]$")
    ] = Field(
        None,
        description=(
            "Time to which molar radioactivity measurement above applies in the"
            ' default\nunit `"hh:mm:ss"`.\n'
        ),
    )
    MolarActivityUnits: Optional[str] = Field(
        None,
        description=(
            'Unit of the specified molar radioactivity (for example, `"GBq/umol"`).\n'
        ),
    )
    MultibandAccelerationFactor: Optional[float] = Field(
        None, description="The multiband factor, for multiband acquisitions.\n"
    )
    MultipartID: Optional[str] = Field(
        None,
        description=(
            "A unique (per participant) label tagging DWI runs that are part of"
            " a\nmultipart scan.\n"
        ),
    )
    Name: Optional[str] = Field(None, description="Name of the dataset.\n")
    NegativeContrast: Optional[bool] = Field(
        None,
        description=(
            "`true` or `false` value specifying whether increasing voxel"
            " intensity\n(within sample voxels) denotes a decreased value with respect"
            " to the\ncontrast suffix.\nThis is commonly the case when Cerebral Blood"
            " Volume is estimated via\nusage of a contrast agent in conjunction with a"
            " T2\\* weighted acquisition\nprotocol.\n"
        ),
    )
    NonlinearGradientCorrection: Optional[bool] = Field(
        None,
        description=(
            "Boolean stating if the image saved has been corrected for"
            " gradient\nnonlinearities by the scanner sequence.\n"
        ),
    )
    NumberOfVolumesDiscardedByScanner: Optional[conint(ge=0)] = Field(
        None,
        description=(
            'Number of volumes ("dummy scans") discarded by the scanner\n(as opposed to'
            " those discarded by the user post hoc)\nbefore saving the imaging"
            " file.\nFor example, a sequence that automatically discards the first 4"
            " volumes\nbefore saving would have this field as 4.\nA sequence that does"
            " not discard dummy scans would have this set to 0.\nPlease note that the"
            " onsets recorded in the `events.tsv` file should always\nrefer to the"
            " beginning of the acquisition of the first volume in the\ncorresponding"
            " imaging file - independent of the value"
            ' of\n`"NumberOfVolumesDiscardedByScanner"` field.\n'
        ),
    )
    NumberOfVolumesDiscardedByUser: Optional[conint(ge=0)] = Field(
        None,
        description=(
            'Number of volumes ("dummy scans") discarded by the user before including'
            " the\nfile in the dataset.\nIf possible, including all of the volumes is"
            " strongly recommended.\nPlease note that the onsets recorded in the"
            " `events.tsv` file should always\nrefer to the beginning of the"
            " acquisition of the first volume in the\ncorresponding imaging file -"
            ' independent of the value of\n`"NumberOfVolumesDiscardedByUser"` field.\n'
        ),
    )
    NumberShots: Optional[Union[float, List[float]]] = Field(
        None,
        description=(
            "The number of RF excitations needed to reconstruct a slice or volume\n(may"
            " be referred to as partition).\nPlease mind that this is not the same as"
            " Echo Train Length which denotes the\nnumber of k-space lines collected"
            " after excitation in a multi-echo readout.\nThe data type array is"
            " applicable for specifying this parameter before and\nafter the k-space"
            ' center is sampled.\nPlease see\n[`"NumberShots"` metadata'
            " field]\\\n(/99-appendices/11-qmri.html#numbershots-metadata-field)\nin"
            " the qMRI appendix for corresponding calculations.\n"
        ),
    )
    NumericalAperture: Optional[PositiveFloat] = Field(
        None,
        description=(
            "Lens numerical aperture (for example: `1.4`). If the file format is"
            " OME-TIFF,\nthe value MUST be consistent with the `LensNA` OME metadata"
            " field.\n"
        ),
    )
    OperatingSystem: Optional[str] = Field(
        None,
        description=(
            "Operating system used to run the stimuli presentation software\n(for"
            " formatting recommendations, see examples below this table).\n"
        ),
    )
    OtherAcquisitionParameters: Optional[str] = Field(
        None,
        description="Description of other relevant image acquisition parameters.\n",
    )
    PASLType: Optional[str] = Field(
        None,
        description=(
            'Type of the labeling pulse of the `PASL` labeling,\nfor example `"FAIR"`,'
            ' `"EPISTAR"`, or `"PICORE"`.\n'
        ),
    )
    PCASLType: Optional[PCASLType] = Field(
        None,
        description="The type of gradient pulses used in the `control` condition.\n",
    )
    ParallelAcquisitionTechnique: Optional[str] = Field(
        None,
        description=(
            'The type of parallel imaging used (for example `"GRAPPA"`,'
            ' `"SENSE"`).\nCorresponds to DICOM Tag 0018, 9078 `Parallel Acquisition'
            " Technique`.\n"
        ),
    )
    ParallelReductionFactorInPlane: Optional[float] = Field(
        None,
        description=(
            "The parallel imaging (for instance, GRAPPA) factor.\nUse the denominator"
            " of the fraction of k-space encoded for each slice.\nFor example, 2 means"
            " half of k-space is encoded.\nCorresponds to DICOM Tag 0018, 9069"
            " `Parallel Reduction Factor In-plane`.\n"
        ),
    )
    PartialFourier: Optional[float] = Field(
        None,
        description=(
            "The fraction of partial Fourier information collected.\nCorresponds to"
            " DICOM Tag 0018, 9081 `Partial Fourier`.\n"
        ),
    )
    PartialFourierDirection: Optional[str] = Field(
        None,
        description=(
            "The direction where only partial Fourier information was"
            " collected.\nCorresponds to DICOM Tag 0018, 9036 `Partial Fourier"
            " Direction`.\n"
        ),
    )
    PharmaceuticalDoseAmount: Optional[Union[float, List[float]]] = Field(
        None, description="Dose amount of pharmaceutical coadministered with tracer.\n"
    )
    PharmaceuticalDoseRegimen: Optional[str] = Field(
        None,
        description=(
            "Details of the pharmaceutical dose regimen.\nEither adequate description"
            " or short-code relating to regimen documented\nelsewhere (for example,"
            ' `"single oral bolus"`).\n'
        ),
    )
    PharmaceuticalDoseTime: Optional[Union[float, List[float]]] = Field(
        None,
        description=(
            "Time of administration of pharmaceutical dose, relative to time zero.\nFor"
            " an infusion, this should be a vector with two elements specifying"
            " the\nstart and end of the infusion period. For more complex dose"
            " regimens,\nthe regimen description should be complete enough to enable"
            ' unambiguous\ninterpretation of `"PharmaceuticalDoseTime"`.\nUnit format'
            " of the specified pharmaceutical dose time MUST be seconds.\n"
        ),
    )
    PharmaceuticalDoseUnits: Optional[str] = Field(
        None,
        description=(
            'Unit format relating to pharmaceutical dose\n(for example, `"mg"` or'
            ' `"mg/kg"`).\n'
        ),
    )
    PharmaceuticalName: Optional[str] = Field(
        None, description="Name of pharmaceutical coadministered with tracer.\n"
    )
    PhaseEncodingDirection: Optional[PhaseEncodingDirection] = Field(
        None,
        description=(
            "The letters `i`, `j`, `k` correspond to the first, second and third axis"
            " of\nthe data in the NIFTI file.\nThe polarity of the phase encoding is"
            " assumed to go from zero index to\nmaximum index unless `-` sign is"
            " present\n(then the order is reversed - starting from the highest index"
            " instead of\nzero).\n`PhaseEncodingDirection` is defined as the direction"
            " along which phase is was\nmodulated which may result in visible"
            " distortions.\nNote that this is not the same as the DICOM"
            " term\n`InPlanePhaseEncodingDirection` which can have `ROW` or `COL`"
            " values.\n"
        ),
    )
    PixelSize: Optional[List[PixelSizeItem]] = Field(
        None,
        description=(
            "A 2- or 3-number array of the physical size of a pixel, either"
            " `[PixelSizeX, PixelSizeY]`\nor `[PixelSizeX, PixelSizeY, PixelSizeZ]`,"
            " where X is the width, Y the height and Z the\ndepth.\nIf the file format"
            " is OME-TIFF, these values need to be consistent with"
            " `PhysicalSizeX`,\n`PhysicalSizeY` and `PhysicalSizeZ` OME metadata"
            " fields, after converting in\n`PixelSizeUnits` according to"
            " `PhysicalSizeXunit`, `PhysicalSizeYunit` and\n`PhysicalSizeZunit` OME"
            " fields.\n"
        ),
        max_items=3,
        min_items=2,
    )
    PixelSizeUnits: Optional[PixelSizeUnits] = Field(
        None,
        description=(
            'Unit format of the specified `"PixelSize"`. MUST be one of: `"mm"`'
            ' (millimeter), `"um"`\n(micrometer) or `"nm"` (nanometer).\n'
        ),
    )
    PlasmaAvail: Optional[bool] = Field(
        None,
        description="Boolean that specifies if plasma measurements are available.\n",
    )
    PlasmaFreeFraction: Optional[confloat(ge=0.0, le=100.0)] = Field(
        None,
        description=(
            "Measured free fraction in plasma, meaning the concentration of free"
            " compound\nin plasma divided by total concentration of compound in"
            " plasma\n(Units: 0-100%).\n"
        ),
    )
    PlasmaFreeFractionMethod: Optional[str] = Field(
        None, description="Method used to estimate free fraction.\n"
    )
    PostLabelingDelay: Optional[Union[PositiveFloat, List[PositiveFloat]]] = Field(
        None,
        description=(
            "This is the postlabeling delay (PLD) time, in seconds, after the end of"
            ' the\nlabeling (for `"CASL"` or `"PCASL"`) or middle of the labeling'
            ' pulse\n(for `"PASL"`) until the middle of the excitation pulse applied to'
            " the\nimaging slab (for 3D acquisition) or first slice (for 2D"
            " acquisition).\nCan be a number (for a single-PLD time series) or an array"
            " of numbers\n(for multi-PLD and Look-Locker).\nIn the latter case, the"
            " array of numbers contains the PLD of each volume,\nnamely each `control`"
            " and `label`, in the acquisition order.\nAny image within the time-series"
            " without a PLD, for example an `m0scan`,\nis indicated by a zero.\nBased"
            " on DICOM Tags 0018, 9079 `Inversion Times` and 0018,"
            " 0082\n`InversionTime`.\n"
        ),
    )
    PowerLineFrequency: Optional[Union[PositiveFloat, PowerLineFrequencyEnum]] = Field(
        None,
        description=(
            "Frequency (in Hz) of the power grid at the geographical location of"
            " the\ninstrument (for example, `50` or `60`).\n"
        ),
    )
    PromptRate: Optional[List[float]] = Field(
        None,
        description=(
            "Prompt rate for each frame (same units as `Units`, for example,"
            ' `"Bq/mL"`).\n'
        ),
    )
    PulseSequenceDetails: Optional[str] = Field(
        None,
        description=(
            "Information beyond pulse sequence type that identifies the specific"
            ' pulse\nsequence used (for example,\n`"Standard Siemens Sequence'
            ' distributed with the VB17 software"`,\n`"Siemens WIP ### version #.##,"`'
            ' or\n`"Sequence written by X using a version compiled on MM/DD/YYYY"`).\n'
        ),
    )
    PulseSequenceType: Optional[str] = Field(
        None,
        description=(
            "A general description of the pulse sequence used for the scan\n(for"
            ' example, `"MPRAGE"`, `"Gradient Echo EPI"`, `"Spin Echo'
            ' EPI"`,\n`"Multiband gradient echo EPI"`).\n'
        ),
    )
    Purity: Optional[confloat(ge=0.0, le=100.0)] = Field(
        None, description="Purity of the radiolabeled compound (between 0 and 100%).\n"
    )
    RandomRate: Optional[List[float]] = Field(
        None,
        description=(
            'Random rate for each frame (same units as `"Units"`, for example,'
            ' `"Bq/mL"`).\n'
        ),
    )
    RawSources: Optional[List[str]] = Field(
        None,
        description=(
            "A list of paths relative to dataset root pointing to the BIDS-Raw"
            " file(s)\nthat were used in the creation of this derivative.\n"
        ),
    )
    ReceiveCoilActiveElements: Optional[str] = Field(
        None,
        description=(
            "Information describing the active/selected elements of the receiver"
            " coil.\nThis does not correspond to a tag in the DICOM ontology.\nThe"
            " vendor-defined terminology for active coil elements can go in this"
            " field.\n"
        ),
    )
    ReceiveCoilName: Optional[str] = Field(
        None,
        description=(
            "Information describing the receiver coil.\nCorresponds to DICOM Tag 0018,"
            " 1250 `Receive Coil Name`,\nalthough not all vendors populate that DICOM"
            " Tag,\nin which case this field can be derived from an"
            " appropriate\nprivate DICOM field.\n"
        ),
    )
    ReconFilterSize: Optional[Union[float, List[float]]] = Field(
        None,
        description=(
            'Kernel size of post-recon filter (FWHM) in default units `"mm"`.\n'
        ),
    )
    ReconFilterType: Optional[Union[str, List[str]]] = Field(
        None, description='Type of post-recon smoothing (for example, `["Shepp"]`).\n'
    )
    ReconMethodImplementationVersion: Optional[str] = Field(
        None,
        description="Identification for the software used, such as name and version.\n",
    )
    ReconMethodName: Optional[str] = Field(
        None,
        description=(
            'Reconstruction method or algorithm (for example, `"3d-op-osem"`).\n'
        ),
    )
    ReconMethodParameterLabels: Optional[List[str]] = Field(
        None,
        description=(
            'Names of reconstruction parameters (for example, `["subsets",'
            ' "iterations"]`).\n'
        ),
    )
    ReconMethodParameterUnits: Optional[List[str]] = Field(
        None,
        description=(
            'Unit of reconstruction parameters (for example, `["none", "none"]`).\n'
        ),
    )
    ReconMethodParameterValues: Optional[List[float]] = Field(
        None,
        description="Values of reconstruction parameters (for example, `[21, 3]`).\n",
    )
    RecordingDuration: Optional[float] = Field(
        None, description="Length of the recording in seconds (for example, `3600`).\n"
    )
    RecordingType: Optional[RecordingType] = Field(
        None,
        description=(
            'Defines whether the recording is `"continuous"`, `"discontinuous"`,'
            ' or\n`"epoched"`, where `"epoched"` is limited to time windows about'
            " events of\ninterest (for example, stimulus presentations or subject"
            " responses).\n"
        ),
    )
    ReferencesAndLinks: Optional[List[str]] = Field(
        None,
        description=(
            "List of references to publications that contain information on the"
            " dataset.\nA reference may be textual or"
            " a\n[URI](/02-common-principles.html#uniform-resource-indicator).\n"
        ),
    )
    RepetitionTime: Optional[PositiveFloat] = Field(
        None,
        description=(
            "The time in seconds between the beginning of an acquisition of one"
            " volume\nand the beginning of acquisition of the volume following it"
            " (TR).\nWhen used in the context of functional acquisitions this parameter"
            " best\ncorresponds to\n[DICOM Tag 0020,"
            " 0110](http://dicomlookup.com/lookup.asp?sw=Tnumber&q=(0020,0110)):\nthe"
            ' "time delta between images in a\ndynamic of functional set of images" but'
            " may also be found in\n[DICOM Tag 0018,"
            ' 0080](http://dicomlookup.com/lookup.asp?sw=Tnumber&q=(0018,0080)):\n"the'
            " period of time in msec between the beginning\nof a pulse sequence and the"
            " beginning of the succeeding\n(essentially identical) pulse"
            ' sequence".\nThis definition includes time between scans (when no data has'
            " been acquired)\nin case of sparse acquisition schemes.\nThis value MUST"
            " be consistent with the 'pixdim[4]' field (after accounting\nfor units"
            " stored in 'xyzt_units' field) in the NIfTI header.\nThis field is"
            " mutually exclusive with VolumeTiming.\n"
        ),
    )
    RepetitionTimeExcitation: Optional[confloat(ge=0.0)] = Field(
        None,
        description=(
            "The interval, in seconds, between two successive excitations.\n[DICOM Tag"
            " 0018,"
            " 0080](http://dicomlookup.com/lookup.asp?sw=Tnumber&q=(0018,0080)\nbest"
            " refers to this parameter.\nThis field may be used together with the"
            ' `"RepetitionTimePreparation"` for\ncertain use cases, such'
            " as\n[MP2RAGE](https://doi.org/10.1016/j.neuroimage.2009.10.002).\nUse"
            " `RepetitionTimeExcitation` (in combination"
            ' with\n`"RepetitionTimePreparation"` if needed) for anatomy imaging data'
            ' rather than\n`"RepetitionTime"` as it is already defined as the amount of'
            " time that it takes\nto acquire a single volume in the\n[task imaging"
            " data](/04-modality-specific-files/01-magnetic-resonance-\\\nimaging-data.html#task-including-resting-state-imaging-data)\nsection.\n"
        ),
    )
    RepetitionTimePreparation: Optional[
        Union[confloat(ge=0.0), List[confloat(ge=0.0)]]
    ] = Field(
        None,
        description=(
            "The interval, in seconds, that it takes a preparation pulse block"
            " to\nre-appear at the beginning of the succeeding (essentially identical)"
            " pulse\nsequence block.\nThe data type number may apply to files from any"
            " MRI modality concerned with\na single value for this field.\nThe data"
            " type array provides a value for each volume in a 4D dataset and\nshould"
            " only be used when the volume timing is critical for interpretation"
            " of\nthe data, such as"
            " in\n[ASL](/04-modality-specific-files/01-magnetic-resonance-imaging-data.html\\\n#arterial-spin-labeling-perfusion-data).\n"
        ),
    )
    Resolution: Optional[Union[str, Dict[str, str]]] = Field(
        None,
        description=(
            "Specifies the interpretation of the resolution keyword.\nIf an object is"
            " used, then the keys should be values for the ``res`` entity\nand values"
            " should be descriptions of those ``res`` values.\n"
        ),
    )
    SEEGChannelCount: Optional[conint(ge=0)] = Field(
        None, description="Number of SEEG channels.\n"
    )
    SampleEmbedding: Optional[str] = Field(
        None,
        description=(
            'Description of the tissue sample embedding (for example: `"Epoxy'
            ' resin"`).\n'
        ),
    )
    SampleEnvironment: Optional[SampleEnvironment] = Field(
        None,
        description=(
            'Environment in which the sample was imaged. MUST be one of: `"in vivo"`,'
            ' `"ex vivo"`\nor `"in vitro"`.\n'
        ),
    )
    SampleExtractionInstitution: Optional[str] = Field(
        None,
        description=(
            "The name of the institution in charge of the extraction of the sample,\nif"
            " different from the institution in charge of the equipment that produced"
            " the image.\n"
        ),
    )
    SampleExtractionProtocol: Optional[str] = Field(
        None,
        description=(
            "Description of the sample extraction protocol"
            " or\n[URI](/02-common-principles.html#uniform-resource-indicator)\n(for"
            " example from [protocols.io](https://www.protocols.io/)).\n"
        ),
    )
    SampleFixation: Optional[str] = Field(
        None,
        description=(
            'Description of the tissue sample fixation\n(for example: `"4%'
            ' paraformaldehyde, 2% glutaraldehyde"`).\n'
        ),
    )
    SampleOrigin: Optional[SampleOrigin] = Field(
        None,
        description=(
            "Describes from which tissue the genetic information was extracted.\n"
        ),
    )
    SamplePrimaryAntibody: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "Description(s) of the primary antibody used for immunostaining.\nEither an"
            " [RRID](https://scicrunch.org/resources) or the name, supplier and"
            " catalogue\nnumber of a commercial antibody.\nFor non-commercial"
            " antibodies either an [RRID](https://scicrunch.org/resources) or"
            ' the\nhost-animal and immunogen used (for examples: `"RRID:AB_2122563"`'
            ' or\n`"Rabbit anti-Human HTR5A Polyclonal Antibody, Invitrogen, Catalog #'
            ' PA1-2453"`).\nMAY be an array of strings if different antibodies are used'
            " in each channel of the file.\n"
        ),
    )
    SampleSecondaryAntibody: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "Description(s) of the secondary antibody used for immunostaining.\nEither"
            " an [RRID](https://scicrunch.org/resources) or the name, supplier and"
            " catalogue\nnumber of a commercial antibody.\nFor non-commercial"
            " antibodies either an [RRID](https://scicrunch.org/resources) or"
            ' the\nhost-animal and immunogen used (for examples: `"RRID:AB_228322"`'
            ' or\n`"Goat anti-Mouse IgM Secondary Antibody, Invitrogen, Catalog #'
            ' 31172"`).\nMAY be an array of strings if different antibodies are used in'
            " each channel of the file.\n"
        ),
    )
    SampleStaining: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "Description(s) of the tissue sample staining (for example:"
            ' `"Osmium"`).\nMAY be an array of strings if different stains are used in'
            ' each channel of the file\n(for example: `["LFB", "PLP"]`).\n'
        ),
    )
    SamplingFrequency: Optional[float] = Field(
        None,
        description=(
            "Sampling frequency (in Hz) of all the data in the recording,\nregardless"
            " of their type (for example, `2400`).\n"
        ),
    )
    ScaleFactor: Optional[List[float]] = Field(
        None, description="Scale factor for each frame.\n"
    )
    ScanDate: Optional[date] = Field(
        None,
        description=(
            'Date of scan in the format `"YYYY-MM-DD[Z]"`.\nThis field is DEPRECATED,'
            " and this metadata SHOULD be recorded in the `acq_time` column of"
            " the\ncorresponding [Scans"
            " file](/03-modality-agnostic-files.html#scans-file).\n"
        ),
    )
    ScanOptions: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "Parameters of ScanningSequence.\nCorresponds to DICOM Tag 0018, 0022 `Scan"
            " Options`.\n"
        ),
    )
    ScanStart: Optional[float] = Field(
        None,
        description=(
            "Time of start of scan with respect to `TimeZero` in the default unit"
            " seconds.\n"
        ),
    )
    ScanningSequence: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "Description of the type of data acquired.\nCorresponds to DICOM Tag 0018,"
            " 0020 `Scanning Sequence`.\n"
        ),
    )
    ScatterFraction: Optional[List[confloat(ge=0.0, le=100.0)]] = Field(
        None, description="Scatter fraction for each frame (Units: 0-100%).\n"
    )
    SequenceName: Optional[str] = Field(
        None,
        description=(
            "Manufacturer's designation of the sequence name.\nCorresponds to DICOM Tag"
            " 0018, 0024 `Sequence Name`.\n"
        ),
    )
    SequenceVariant: Optional[Union[str, List[str]]] = Field(
        None,
        description=(
            "Variant of the ScanningSequence.\nCorresponds to DICOM Tag 0018, 0021"
            " `Sequence Variant`.\n"
        ),
    )
    SinglesRate: Optional[List[float]] = Field(
        None,
        description=(
            "Singles rate for each frame (same units as `Units`, for example,"
            ' `"Bq/mL"`).\n'
        ),
    )
    SkullStripped: Optional[bool] = Field(
        None,
        description=(
            "Whether the volume was skull stripped (non-brain voxels set to zero) or"
            " not.\n"
        ),
    )
    SliceEncodingDirection: Optional[SliceEncodingDirection] = Field(
        None,
        description=(
            "The axis of the NIfTI data along which slices were acquired,\nand the"
            ' direction in which `"SliceTiming"` is defined with respect to.\n`i`, `j`,'
            " `k` identifiers correspond to the first, second and third axis of\nthe"
            " data in the NIfTI file.\nA `-` sign indicates that the contents of"
            ' `"SliceTiming"` are defined in\nreverse order - that is, the first entry'
            " corresponds to the slice with the\nlargest index, and the final entry"
            " corresponds to slice index zero.\nWhen present, the axis defined by"
            ' `"SliceEncodingDirection"` needs to be\nconsistent with the `slice_dim`'
            ' field in the NIfTI header.\nWhen absent, the entries in `"SliceTiming"`'
            " must be in the order of increasing\nslice index as defined by the NIfTI"
            " header.\n"
        ),
    )
    SliceThickness: Optional[PositiveFloat] = Field(
        None,
        description=(
            'Slice thickness of the tissue sample in the unit micrometers (`"um"`) (for'
            " example: `5`).\n"
        ),
    )
    SliceTiming: Optional[List[confloat(ge=0.0)]] = Field(
        None,
        description=(
            "The time at which each slice was acquired within each volume (frame) of"
            " the\nacquisition.\nSlice timing is not slice order -- rather, it is a"
            " list of times containing\nthe time (in seconds) of each slice acquisition"
            " in relation to the beginning\nof volume acquisition.\nThe list goes"
            " through the slices along the slice axis in the slice encoding\ndimension"
            " (see below).\nNote that to ensure the proper interpretation of the"
            ' `"SliceTiming"` field,\nit is important to check if the OPTIONAL'
            " `SliceEncodingDirection` exists.\nIn particular, if"
            ' `"SliceEncodingDirection"` is negative,\nthe entries in `"SliceTiming"`'
            " are defined in reverse order with respect to the\nslice axis, such that"
            ' the final entry in the `"SliceTiming"` list is the time\nof acquisition'
            " of slice 0. Without this parameter slice time correction will\nnot be"
            " possible.\n"
        ),
    )
    SoftwareFilters: Optional[Union[Dict[str, Dict[str, Any]], SoftwareFilter]] = Field(
        None,
        description=(
            "[Object](https://www.json.org/json-en.html)\nof temporal software filters"
            ' applied, or `"n/a"` if the data is\nnot available.\nEach key:value pair'
            " in the JSON object is a name of the filter and an object\nin which its"
            ' parameters are defined as key:value pairs\n(for example, `{"Anti-aliasing'
            ' filter":\n{"half-amplitude cutoff (Hz)": 500, "Roll-off":'
            ' "6dB/Octave"}}`).\n'
        ),
    )
    SoftwareName: Optional[str] = Field(
        None, description="Name of the software that was used to present the stimuli.\n"
    )
    SoftwareRRID: Optional[constr(regex=r".+_.+")] = Field(
        None,
        description=(
            "[Research Resource Identifier](https://scicrunch.org/resources) of"
            " the\nsoftware that was used to present the stimuli.\nExamples: The RRID"
            " for Psychtoolbox is 'SCR_002881',\nand that of PsychoPy is"
            " 'SCR_006571'.\n"
        ),
    )
    SoftwareVersion: Optional[str] = Field(
        None,
        description="Version of the software that was used to present the stimuli.\n",
    )
    SoftwareVersions: Optional[str] = Field(
        None,
        description=(
            "Manufacturer's designation of software version of the equipment that"
            " produced\nthe measurements.\n"
        ),
    )
    SourceDatasets: Optional[List[SourceDataset]] = Field(
        None,
        description=(
            "Used to specify the locations and relevant attributes of all source"
            ' datasets.\nValid keys in each object include `"URL"`, `"DOI"`'
            " (see\n[URI](/02-common-principles.html#uniform-resource-indicator)),"
            ' and\n`"Version"`'
            " with\n[string](https://www.w3schools.com/js/js_json_datatypes.asp)\nvalues.\n"
        ),
    )
    Sources: Optional[List[str]] = Field(
        None,
        description=(
            "A list of files with the paths specified relative to dataset root;\nthese"
            " files were directly used in the creation of this derivative data"
            " file.\nFor example, if a derivative A is used in the creation of"
            " another\nderivative B, which is in turn used to generate C in a chain of"
            ' A->B->C,\nC should only list B in `"Sources"`, and B should only list A'
            ' in `"Sources"`.\nHowever, in case both X and Y are directly used in the'
            ' creation of Z,\nthen Z should list X and Y in `"Sources"`,\nregardless of'
            " whether X was used to generate Y.\n"
        ),
    )
    SpatialReference: Optional[
        Union[
            SpatialReferenceEnum,
            AnyUrl,
            str,
            Dict[str, Union[SpatialReferenceEnum1, AnyUrl, str]],
        ]
    ] = Field(
        None,
        description=(
            "For images with a single reference, the value MUST be a single"
            " string.\nFor images with multiple references, such as surface and volume"
            " references,\na JSON object MUST be used.\n"
        ),
    )
    SpecificRadioactivity: Optional[Union[float, SpecificRadioactivityEnum]] = Field(
        None,
        description=(
            "Specific activity of compound injected.\n**Note this is not required for"
            " an FDG acquisition, since it is not available,\nand SHOULD be set to"
            ' `"n/a"`**.\n'
        ),
    )
    SpecificRadioactivityMeasTime: Optional[
        constr(regex=r"^(?:2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]$")
    ] = Field(
        None,
        description=(
            "Time to which specific radioactivity measurement above applies in the"
            ' default\nunit `"hh:mm:ss"`.\n'
        ),
    )
    SpecificRadioactivityUnits: Optional[Union[str, SpecificRadioactivityUnit]] = Field(
        None,
        description=(
            "Unit format of specified specific radioactivity (for example,"
            ' `"Bq/g"`).\n**Note this is not required for an FDG acquisition, since it'
            ' is not available,\nand SHOULD be set to `"n/a"`**.\n'
        ),
    )
    SpoilingGradientDuration: Optional[float] = Field(
        None,
        description=(
            "The duration of the spoiler gradient lobe in seconds.\nThe duration of a"
            " trapezoidal lobe is defined as the summation of ramp-up\nand plateau"
            " times.\n"
        ),
    )
    SpoilingGradientMoment: Optional[float] = Field(
        None,
        description=(
            "Zeroth moment of the spoiler gradient lobe in\nmillitesla times second per"
            " meter (mT.s/m).\n"
        ),
    )
    SpoilingRFPhaseIncrement: Optional[float] = Field(
        None,
        description=(
            "The amount of incrementation described in degrees,\nwhich is applied to"
            " the phase of the excitation pulse at each TR period for\nachieving RF"
            " spoiling.\n"
        ),
    )
    SpoilingState: Optional[bool] = Field(
        None,
        description=(
            "Boolean stating whether the pulse sequence uses any type of"
            " spoiling\nstrategy to suppress residual transverse magnetization.\n"
        ),
    )
    SpoilingType: Optional[SpoilingType] = Field(
        None,
        description=(
            "Specifies which spoiling method(s) are used by a spoiled sequence.\n"
        ),
    )
    StartTime: Optional[float] = Field(
        None,
        description=(
            "Start time in seconds in relation to the start of acquisition of the"
            " first\ndata sample in the corresponding neural dataset (negative values"
            " are allowed).\n"
        ),
    )
    StationName: Optional[str] = Field(
        None,
        description=(
            "Institution defined name of the machine that produced the measurements.\n"
        ),
    )
    StimulusPresentation: Optional[StimulusPresentation] = Field(
        None,
        description=(
            "Object containing key value pairs related to the software used to"
            " present\nthe stimuli during the experiment,"
            ' specifically:\n`"OperatingSystem"`, `"SoftwareName"`, `"SoftwareRRID"`,'
            ' `"SoftwareVersion"` and\n`"Code"`.\nSee table below for more'
            " information.\n"
        ),
    )
    SubjectArtefactDescription: Optional[str] = Field(
        None,
        description=(
            "Freeform description of the observed subject artefact and its possible"
            ' cause\n(for example, `"Vagus Nerve Stimulator"`, `"non-removable'
            ' implant"`).\nIf this field is set to `"n/a"`, it will be interpreted as'
            " absence of major\nsource of artifacts except cardiac and blinks.\n"
        ),
    )
    TaskDescription: Optional[str] = Field(
        None, description="Longer description of the task.\n"
    )
    TaskName: Optional[str] = Field(
        None,
        description=(
            "Name of the task.\nNo two tasks should have the same name.\nThe task label"
            ' included in the file name is derived from this `"TaskName"` field\nby'
            " removing all non-alphanumeric (`[a-zA-Z0-9]`) characters.\nFor example"
            ' `"TaskName"` `"faces n-back"` will correspond to task'
            " label\n`facesnback`.\n"
        ),
    )
    TermURL: Optional[str] = Field(
        None,
        description=(
            "URL pointing to a formal definition of this type of data in an"
            " ontology\navailable on the web.\n"
        ),
    )
    TimeZero: Optional[
        constr(regex=r"^(?:2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]$")
    ] = Field(
        None,
        description=(
            "Time zero to which all scan and/or blood measurements have been adjusted"
            ' to,\nin the unit "hh:mm:ss".\nThis should be equal to `"InjectionStart"`'
            ' or `"ScanStart"`.\n'
        ),
    )
    TissueDeformationScaling: Optional[PositiveFloat] = Field(
        None,
        description=(
            "Estimated deformation of the tissue, given as a percentage of the"
            " original\ntissue size (for examples: for a shrinkage of 3%, the value is"
            " `97`;\nand for an expansion of 100%, the value is `200`).\n"
        ),
    )
    TissueOrigin: Optional[TissueOrigin] = Field(
        None,
        description=(
            'Describes the type of tissue analyzed for `"SampleOrigin"` `brain`.\n'
        ),
    )
    TotalAcquiredPairs: Optional[PositiveFloat] = Field(
        None,
        description=(
            "The total number of acquired `control`-`label` pairs.\nA single pair"
            " consists of a single `control` and a single `label` image.\n"
        ),
    )
    TotalReadoutTime: Optional[float] = Field(
        None,
        description=(
            'This is actually the "effective" total readout time,\ndefined as the'
            " readout duration, specified in seconds,\nthat would have generated data"
            " with the given level of distortion.\nIt is NOT the actual, physical"
            ' duration of the readout train.\nIf `"EffectiveEchoSpacing"` has been'
            " properly computed,\nit is just `EffectiveEchoSpacing * (ReconMatrixPE -"
            " 1)`.\n"
        ),
    )
    TracerMolecularWeight: Optional[float] = Field(
        None, description="Accurate molecular weight of the tracer used.\n"
    )
    TracerMolecularWeightUnits: Optional[str] = Field(
        None,
        description=(
            'Unit of the molecular weights measurement (for example, `"g/mol"`).\n'
        ),
    )
    TracerName: Optional[str] = Field(
        None,
        description='Name of the tracer compound used (for example, `"CIMBI-36"`)\n',
    )
    TracerRadLex: Optional[str] = Field(
        None, description="ID of the tracer compound from the RadLex Ontology.\n"
    )
    TracerRadionuclide: Optional[str] = Field(
        None, description='Radioisotope labelling tracer (for example, `"C11"`).\n'
    )
    TracerSNOMED: Optional[str] = Field(
        None,
        description=(
            "ID of the tracer compound from the SNOMED Ontology\n(subclass of"
            " Radioactive isotope).\n"
        ),
    )
    TriggerChannelCount: Optional[conint(ge=0)] = Field(
        None, description="Number of channels for digital (TTL bit level) triggers.\n"
    )
    TubingLength: Optional[float] = Field(
        None,
        description=(
            "The length of the blood tubing, from the subject to the detector in"
            " meters.\n"
        ),
    )
    TubingType: Optional[str] = Field(
        None,
        description=(
            "Description of the type of tubing used, ideally including the material"
            " and\n(internal) diameter.\n"
        ),
    )
    Type: Optional[Type] = Field(
        None,
        description=(
            'Short identifier of the mask.\nThe value `"Brain"` refers to a brain'
            ' mask.\nThe value `"Lesion"` refers to a lesion mask.\nThe value `"Face"`'
            ' refers to a face mask.\nThe value `"ROI"` refers to a region of interest'
            " mask.\n"
        ),
    )
    Units: Optional[str] = Field(
        None,
        description=(
            "Measurement units for the associated file.\nSI units in CMIXF formatting"
            " are RECOMMENDED\n(see [Units](/02-common-principles.html#units)).\n"
        ),
    )
    VascularCrushing: Optional[bool] = Field(
        None,
        description=(
            "Boolean indicating if Vascular Crushing is used.\nCorresponds to DICOM Tag"
            " 0018, 9259 `ASL Crusher Flag`.\n"
        ),
    )
    VascularCrushingVENC: Optional[Union[float, List[float]]] = Field(
        None,
        description=(
            "The crusher gradient strength, in centimeters per second.\nSpecify either"
            " one number for the total time-series, or provide an array of\nnumbers,"
            " for example when using QUASAR, using the value zero to identify\nvolumes"
            " for which `VascularCrushing` was turned off.\nCorresponds to DICOM Tag"
            " 0018, 925A `ASL Crusher Flow Limit`.\n"
        ),
    )
    VolumeTiming: Optional[List[float]] = Field(
        None,
        description=(
            "The time at which each volume was acquired during the acquisition.\nIt is"
            " described using a list of times referring to the onset of each volume\nin"
            " the BOLD series.\nThe list must have the same length as the BOLD"
            " series,\nand the values must be non-negative and monotonically"
            ' increasing.\nThis field is mutually exclusive with `"RepetitionTime"` and'
            ' `"DelayTime"`.\nIf defined, this requires acquisition time (TA) be'
            ' defined via either\n`"SliceTiming"` or `"AcquisitionDuration"` be'
            " defined.\n"
        ),
        min_items=1,
    )
    WholeBloodAvail: Optional[bool] = Field(
        None,
        description=(
            "Boolean that specifies if whole blood measurements are available.\nIf"
            " `true`, the `whole_blood_radioactivity` column MUST be present in"
            " the\ncorresponding `*_blood.tsv` file.\n"
        ),
    )
    WithdrawalRate: Optional[float] = Field(
        None,
        description=(
            "The rate at which the blood was withdrawn from the subject.\nThe unit of"
            ' the specified withdrawal rate should be in `"mL/s"`.\n'
        ),
    )
    _CoordUnits: Optional[_CoordUnits] = None
    _EEGCoordSys: Optional[_EEGCoordSys] = None
    _GeneticLevelEnum: Optional[_GeneticLevelEnum] = None
    _LandmarkCoordinates: Optional[Dict[str, List[float]]] = None
    _MEGCoordSys: Optional[_MEGCoordSys] = None
    _StandardTemplateCoordSys: Optional[_StandardTemplateCoordSys] = None
    _StandardTemplateDeprecatedCoordSys: Optional[
        _StandardTemplateDeprecatedCoordSys
    ] = None
    _iEEGCoordSys: Optional[_IEEGCoordSys] = None
    iEEGCoordinateProcessingDescription: Optional[str] = Field(
        None,
        description=(
            "Has any post-processing (such as projection) been done on the"
            ' electrode\npositions (for example, `"surface_projection"`, `"none"`).\n'
        ),
    )
    iEEGCoordinateProcessingReference: Optional[str] = Field(
        None,
        description=(
            "A reference to a paper that defines in more detail the method used"
            " to\nlocalize the electrodes and to post-process the electrode"
            " positions.\n"
        ),
    )
    iEEGCoordinateSystem: Optional[Union[Any, Any, Any]] = Field(
        None,
        description=(
            "Defines the coordinate system for the iEEG sensors.\nSee\n[Appendix"
            " VIII](/99-appendices/08-coordinate-systems.html)\nfor a list of"
            ' restricted keywords for coordinate systems.\nIf `"Other"`, provide'
            " definition of the coordinate system"
            " in\n`iEEGCoordinateSystemDescription`.\nIf positions correspond to pixel"
            " indices in a 2D image\n(of either a volume-rendering, surface-rendering,"
            ' operative photo, or\noperative drawing), this MUST be `"Pixels"`.\nFor'
            " more information, see the section on\n[2D coordinate"
            " systems](/04-modality-specific-files/04-intracranial\\\n-electroencephalography.html#allowed-2d-coordinate-systems).\n"
        ),
    )
    iEEGCoordinateSystemDescription: Optional[str] = Field(
        None,
        description=(
            "Free-form text description of the coordinate system.\nMay also include a"
            " link to a documentation page or paper describing the\nsystem in greater"
            " detail.\n"
        ),
    )
    iEEGCoordinateUnits: Optional[IEEGCoordinateUnits] = Field(
        None,
        description=(
            'Units of the `*_electrodes.tsv`.\nMUST be `"pixels"` if'
            " `iEEGCoordinateSystem` is `Pixels`.\n"
        ),
    )
    iEEGElectrodeGroups: Optional[str] = Field(
        None,
        description=(
            "Field to describe the way electrodes are grouped into strips, grids or"
            ' depth\nprobes.\nFor example, `"grid1: 10x8 grid on left temporal pole,'
            ' strip2: 1x8 electrode\nstrip on xxx"`.\n'
        ),
    )
    iEEGGround: Optional[str] = Field(
        None,
        description=(
            'Description of the location of the ground electrode\n(`"placed on right'
            ' mastoid (M2)"`).\n'
        ),
    )
    iEEGPlacementScheme: Optional[str] = Field(
        None,
        description=(
            "Freeform description of the placement of the iEEG"
            ' electrodes.\nLeft/right/bilateral/depth/surface\n(for example, `"left'
            ' frontal grid and bilateral hippocampal depth"` or\n`"surface strip and'
            ' STN depth"` or\n`"clinical indication bitemporal, bilateral temporal'
            ' strips and left grid"`).\n'
        ),
    )
    iEEGReference: Optional[str] = Field(
        None,
        description=(
            "General description of the reference scheme used and (when applicable)"
            " of\nlocation of the reference electrode in the raw recordings\n(for"
            ' example, `"left mastoid"`, `"bipolar"`,\n`"T01"` for electrode with name'
            ' T01,\n`"intracranial electrode on top of a grid, not included with'
            ' data"`,\n`"upside down electrode"`).\nIf different channels have a'
            " different reference,\nthis field should have a general description and"
            " the channel specific\nreference should be defined in the `channels.tsv`"
            " file.\n"
        ),
    )
