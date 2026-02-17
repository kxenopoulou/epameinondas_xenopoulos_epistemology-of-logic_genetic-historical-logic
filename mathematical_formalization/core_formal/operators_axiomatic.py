"""
AXIOMATIC OPERATOR DEFINITIONS - CORE FORMAL SIGNATURES
Minimal core: ONLY dialectical operator signatures WITHOUT ANY implementation

================================================================================
CRITICAL ARCHITECTURAL DIRECTIVE:
This file defines the INCONTROVERTIBLE CORE. It MUST NOT be extended directly.
All extensions (temporal, praxis, modal, etc.) MUST live in separate modules.
================================================================================

CORE PRINCIPLES:
1. Define ONLY operator TYPES (signatures)
2. NO implementations, NO algorithms, NO computations  
3. NO praxis, NO temporal, NO becoming, NO context
4. PURELY structural/formal definitions

Violating these principles destroys the philosophical integrity of the system.
"""

from typing import Set
from dataclasses import dataclass, field
from enum import Enum, auto

# ============================================================================
# 1. CORE OPERATOR TYPES - PURE CATEGORIES
# ============================================================================

class OperatorCategory(Enum):
    """Core categories of operators - ONLY structural properties"""
    TRUTH_FUNCTIONAL = auto()     # Maps truth values to truth values
    DIALECTICAL = auto()          # Handles contradiction, synthesis
    
    @property
    def is_dialectical(self) -> bool:
        """Structural property only"""
        return self == OperatorCategory.DIALECTICAL

class OperatorArity(Enum):
    """Arity of operators - structural property ONLY"""
    UNARY = auto()      # ¬P
    BINARY = auto()     # P ∧ Q  
    
    @property
    def is_fixed(self) -> bool:
        """Structural property"""
        return True  # Core only has fixed arity

# ============================================================================
# 2. OPERATOR SIGNATURES - CORE FORMS ONLY
# ============================================================================

@dataclass(frozen=True)
class OperatorSignature:
    """
    Formal SIGNATURE of an operator - CORE DEFINITION ONLY.
    
    Defines WHAT the operator is (formally),
    not HOW it works (algorithmically).
    
    NO context, NO praxis, NO temporal, NO implementation.
    """
    symbol: str          # Formal symbol: ¬ᴰ, ∧ᴰ, ⤊
    name: str            # Formal name: "dialectical_negation"
    category: OperatorCategory
    arity: OperatorArity
    
    # Input/Output types (formal ONLY)
    input_types: Set[str]   # e.g., {"TruthPosition"}
    output_type: str        # e.g., "TruthPosition"
    
    # Structural properties ONLY
    preserves_contradiction: bool = False
    resolves_contradiction: bool = False
    
    # Axioms associated with this operator (formal statements ONLY)
    axioms: Set[str] = field(default_factory=set)
    
    def __str__(self) -> str:
        return f"{self.symbol} ({self.name})"

# ============================================================================
# 3. CORE DIALECTICAL OPERATOR SIGNATURES - THE ABSOLUTE MINIMUM
# ============================================================================

# Classical operators (for contrast only - they are NOT dialectical)
CLASSICAL_NEGATION = OperatorSignature(
    symbol="¬",
    name="classical_negation",
    category=OperatorCategory.TRUTH_FUNCTIONAL,
    arity=OperatorArity.UNARY,
    input_types={"TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=False,
    axioms={"¬¬P ≡ P", "P ∨ ¬P"}  # Classical axioms only
)

# DIALECTICAL CORE OPERATORS
DIALECTICAL_NEGATION = OperatorSignature(
    symbol="¬ᴰ",
    name="dialectical_negation",
    category=OperatorCategory.DIALECTICAL,
    arity=OperatorArity.UNARY,
    input_types={"TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=True,  # Negation PRESERVES contradiction
    axioms={
        "¬ᴰP expresses real opposition, not logical complement",
        "¬ᴰP is defined in relation to P, not as complement of P"
    }
)

DIALECTICAL_CONJUNCTION = OperatorSignature(
    symbol="∧ᴰ",
    name="dialectical_conjunction",
    category=OperatorCategory.DIALECTICAL,
    arity=OperatorArity.BINARY,
    input_types={"TruthPosition", "TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=True,  # Conjunction of opposites CREATES contradiction
    axioms={
        "P ∧ᴰ ¬ᴰP represents real contradiction",
        "∧ᴰ handles opposing tendencies, not just truth values"
    }
)

AUFHEBUNG = OperatorSignature(
    symbol="⤊",
    name="aufhebung",
    category=OperatorCategory.DIALECTICAL,
    arity=OperatorArity.BINARY,
    input_types={"TruthPosition", "TruthPosition"},
    output_type="TruthPosition",
    preserves_contradiction=False,  # Synthesis does NOT preserve contradiction
    resolves_contradiction=True,    # Synthesis RESOLVES contradiction
    axioms={
        "⤊(P, ¬ᴰP) preserves aspects of both P and ¬ᴰP",
        "⤊(P, ¬ᴰP) cancels the contradictory relation",
        "⤊(P, ¬ᴰP) elevates to a new position"
    }
)

# ============================================================================
# 4. CORE OPERATOR RELATIONS - STRUCTURAL ONLY
# ============================================================================

@dataclass(frozen=True)
class OperatorRelation:
    """
    Formal relation BETWEEN operators - STRUCTURAL ONLY.
    
    NO context, NO temporal, NO praxis.
    """
    operator_A: OperatorSignature
    operator_B: OperatorSignature
    relation_type: str  # "specialization", "generalization", "duality"
    
    # Constraints on the relation (formal statements ONLY)
    constraints: Set[str] = field(default_factory=set)

# Core operator relations (structural ONLY)
CORE_OPERATOR_RELATIONS = [
    # Classical negation is a special case of dialectical negation
    OperatorRelation(
        operator_A=CLASSICAL_NEGATION,
        operator_B=DIALECTICAL_NEGATION,
        relation_type="specialization",
        constraints={
            "When contradiction is excluded",
            "When opposition is reduced to logical complement"
        }
    )
]

# ============================================================================
# 5. CORE OPERATOR FAMILIES - STRUCTURAL GROUPINGS ONLY
# ============================================================================

@dataclass(frozen=True)
class OperatorFamily:
    """
    Family of related operators - STRUCTURAL ONLY.
    
    NO context, NO praxis, NO temporal.
    """
    name: str
    members: Set[OperatorSignature]
    common_properties: Set[str] = field(default_factory=set)

# Core operator families
DIALECTICAL_FAMILY = OperatorFamily(
    name="dialectical_family",
    members={DIALECTICAL_NEGATION, DIALECTICAL_CONJUNCTION, AUFHEBUNG},
    common_properties={
        "category: DIALECTICAL",
        "handles_contradiction: True",
        "non_classical: True"
    }
)

NEGATION_FAMILY = OperatorFamily(
    name="negation_family",
    members={CLASSICAL_NEGATION, DIALECTICAL_NEGATION},
    common_properties={
        "arity: UNARY",
        "operation: negation",
        "input: TruthPosition, output: TruthPosition"
    }
)

# ============================================================================
# 6. CORE EXPORTS - ONLY THE ESSENTIALS
# ============================================================================

__all__ = [
    # Operator types
    'OperatorCategory',
    'OperatorArity',
    
    # Core signatures
    'OperatorSignature',
    'CLASSICAL_NEGATION',          # For contrast only
    'DIALECTICAL_NEGATION',        # Core dialectical
    'DIALECTICAL_CONJUNCTION',     # Core dialectical  
    'AUFHEBUNG',                   # Core dialectical
    
    # Core relations
    'OperatorRelation',
    'CORE_OPERATOR_RELATIONS',
    
    # Core families
    'OperatorFamily',
    'DIALECTICAL_FAMILY',
    'NEGATION_FAMILY'
]

# ============================================================================
# 7. USAGE EXAMPLE (Structural only - NO implementation)
# ============================================================================

if __name__ == "__main__":
    """Demonstrate CORE structural properties WITHOUT ANY implementation"""
    
    print("=== CORE DIALECTICAL OPERATORS (Formal Signatures ONLY) ===")
    for op in [DIALECTICAL_NEGATION, DIALECTICAL_CONJUNCTION, AUFHEBUNG]:
        print(f"\n{op.symbol}: {op.name}")
        print(f"  Category: {op.category.name}")
        print(f"  Arity: {op.arity.name}")
        print(f"  Preserves contradiction: {op.preserves_contradiction}")
        print(f"  Resolves contradiction: {op.resolves_contradiction}")
        print(f"  Axioms: {list(op.axioms)}")
    
    print("\n=== CORE OPERATOR FAMILIES ===")
    print(f"\n{DIALECTICAL_FAMILY.name}:")
    for member in DIALECTICAL_FAMILY.members:
        print(f"  - {member.symbol} ({member.name})")
    
    print("\n=== FORMAL RELATIONS ===")
    for rel in CORE_OPERATOR_RELATIONS:
        print(f"\n{rel.operator_A.symbol} is {rel.relation_type} of {rel.operator_B.symbol}")
        for constraint in rel.constraints:
            print(f"  When: {constraint}")
