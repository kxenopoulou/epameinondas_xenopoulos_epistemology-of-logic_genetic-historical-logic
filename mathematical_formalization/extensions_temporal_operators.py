"""
TEMPORAL OPERATORS EXTENSION
Extends core operators with temporal/dynamic aspects.

PRINCIPLES:
1. ALL temporal operators REQUIRE temporal context
2. Time is treated FORMALLY (signatures only)
3. NO implementation of time flow, NO simulation
"""

from typing import Set
from dataclasses import dataclass, field
from enum import Enum, auto

from core_formal.operators_axiomatic import (
    OperatorSignature, OperatorCategory, OperatorArity
)

# ============================================================================
# 1. TEMPORAL CATEGORIES
# ============================================================================

class TemporalCategory(Enum):
    """Categories of temporal operators - structural only"""
    STATIC_MODAL = auto()      # □, ◇ (timeless modality)
    PROCESSUAL = auto()        # →⃗ (becoming as process)
    INTERVAL_BASED = auto()    # Temporal intervals
    
    @property
    def is_processual(self) -> bool:
        return self == TemporalCategory.PROCESSUAL

# ============================================================================
# 2. TEMPORAL OPERATOR SIGNATURES
# ============================================================================

# Static temporal/modal operators
ALWAYS = OperatorSignature(
    symbol="□",
    name="always",
    category=OperatorCategory.TRUTH_FUNCTIONAL,  # Modal, not dialectical
    arity=OperatorArity.UNARY,
    input_types={"TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=False,
    resolves_contradiction=False,
    axioms={
        "□P means P in all temporal positions",
        "□P requires temporal scope specification",
        "In classical systems: □P ≡ ¬◇¬P"
    }
)

EVENTUALLY = OperatorSignature(
    symbol="◇",
    name="eventually",
    category=OperatorCategory.TRUTH_FUNCTIONAL,
    arity=OperatorArity.UNARY,
    input_types={"TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=False,
    resolves_contradiction=False,
    axioms={
        "◇P means P in some temporal position",
        "◇P does not specify which temporal position",
        "In dialectical systems: ◇¬P does not imply ¬□P"
    }
)

# Processual (dialectical temporal) operators
BECOMING = OperatorSignature(
    symbol="→⃗",
    name="becoming",
    category=OperatorCategory.DIALECTICAL,
    arity=OperatorArity.UNARY,
    input_types={"TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=True,  # Becoming preserves contradiction
    resolves_contradiction=False,
    axioms={
        "→⃗P indicates P in process of change",
        "→⃗P is not a state but a movement",
        "→⃗P has internal temporal dynamics"
    }
)

TEMPORAL_SYNTHESIS = OperatorSignature(
    symbol="↝",
    name="temporal_synthesis",
    category=OperatorCategory.DIALECTICAL,
    arity=OperatorArity.BINARY,
    input_types={"TruthPosition", "TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=False,
    resolves_contradiction=True,
    axioms={
        "P ↝ Q represents temporal development of P into Q",
        "P ↝ Q may involve both preservation and transformation",
        "↝ is temporal counterpart of aufhebung"
    }
)

# ============================================================================
# 3. TEMPORAL OPERATOR RELATIONS
# ============================================================================

@dataclass(frozen=True)
class TemporalRelation:
    """Temporal relation between operators - FORMAL ONLY"""
    operator_A: OperatorSignature
    operator_B: OperatorSignature
    temporal_relation: str  # "precedes", "succeeds", "coincides", "during"
    
    # Formal constraints
    constraints: Set[str] = field(default_factory=set)

TEMPORAL_OPERATOR_RELATIONS = [
    TemporalRelation(
        operator_A=ALWAYS,
        operator_B=EVENTUALLY,
        temporal_relation="succeeds",  # □ succeeds ◇ in logical strength
        constraints={"In classical modal logic", "Not necessarily in dialectical"}
    ),
    TemporalRelation(
        operator_A=BECOMING,
        operator_B=TEMPORAL_SYNTHESIS,
        temporal_relation="precedes",  # Becoming precedes synthesis
        constraints={"In Hegelian dialectics", "As temporal process"}
    )
]

# ============================================================================
# 4. TEMPORAL COMPOSITIONS WITH CORE OPERATORS
# ============================================================================

@dataclass(frozen=True)
class TemporalComposition:
    """Temporal composition of operators - FORMAL ONLY"""
    temporal_operator: OperatorSignature
    core_operator: OperatorSignature
    composition_type: str  # "temporal_prefix", "temporal_suffix", "temporal_wrap"
    
    # Validity conditions (formal only)
    is_valid: bool
    validity_conditions: Set[str]
    
    # Resulting operator signature
    resulting_signature: OperatorSignature

from core_formal.operators_axiomatic import DIALECTICAL_NEGATION, AUFHEBUNG

TEMPORAL_COMPOSITIONS = [
    # Becoming of negation
    TemporalComposition(
        temporal_operator=BECOMING,
        core_operator=DIALECTICAL_NEGATION,
        composition_type="temporal_prefix",
        is_valid=True,
        validity_conditions={
            "When negation itself is in process",
            "When time is internal to the negation"
        },
        resulting_signature=OperatorSignature(
            symbol="→⃗¬ᴰ",
            name="becoming_negation",
            category=OperatorCategory.DIALECTICAL,
            arity=OperatorArity.UNARY,
            input_types={"TruthPosition"},
            output_type="TruthPosition",
            preserves_contradiction=True,
            axioms={
                "→⃗¬ᴰP expresses negation as temporal process",
                "→⃗¬ᴰP has its own becoming dynamics"
            }
        )
    ),
    
    # Always-synthesis composition
    TemporalComposition(
        temporal_operator=ALWAYS,
        core_operator=AUFHEBUNG,
        composition_type="temporal_prefix",
        is_valid=True,
        validity_conditions={
            "When synthesis is temporally universal",
            "When aufhebung holds across all times"
        },
        resulting_signature=OperatorSignature(
            symbol="□⤊",
            name="always_synthesis",
            category=OperatorCategory.DIALECTICAL,
            arity=OperatorArity.BINARY,
            input_types={"TruthPosition", "TruthPosition"},
            output_type="TruthPosition",
            preserves_contradiction=False,
            resolves_contradiction=True,
            axioms={
                "□⤊(P, Q) means synthesis holds for all times",
                "□⤊ involves temporal persistence of synthesis"
            }
        )
    )
]

# ============================================================================
# 5. TEMPORAL FAMILIES
# ============================================================================

@dataclass(frozen=True)
class TemporalFamily:
    """Family of temporal operators"""
    name: str
    members: Set[OperatorSignature]
    temporal_properties: Set[str] = field(default_factory=set)

TEMPORAL_FAMILIES = [
    TemporalFamily(
        name="modal_temporal",
        members={ALWAYS, EVENTUALLY},
        temporal_properties={"point-based", "truth-functional", "static"}
    ),
    TemporalFamily(
        name="processual_temporal",
        members={BECOMING, TEMPORAL_SYNTHESIS},
        temporal_properties={"interval-based", "dialectical", "dynamic"}
    )
]

# ============================================================================
# 6. EXPORTS
# ============================================================================

__all__ = [
    # Temporal categories
    'TemporalCategory',
    
    # Temporal operators
    'ALWAYS',
    'EVENTUALLY',
    'BECOMING',
    'TEMPORAL_SYNTHESIS',
    
    # Temporal relations
    'TemporalRelation',
    'TEMPORAL_OPERATOR_RELATIONS',
    
    # Temporal compositions
    'TemporalComposition',
    'TEMPORAL_COMPOSITIONS',
    
    # Temporal families
    'TemporalFamily',
    'TEMPORAL_FAMILIES'
]
