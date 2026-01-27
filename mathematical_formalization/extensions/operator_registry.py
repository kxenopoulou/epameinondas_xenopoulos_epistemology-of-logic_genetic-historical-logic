"""
OPERATOR REGISTRY - UTILITY LAYER
Utility for managing operator signatures across all layers.

PRINCIPLES:
1. PURELY structural indexing
2. NO interpretation, NO computation
3. Separate from core definitions
"""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field

from core_formal.operators_axiomatic import (
    OperatorSignature, OperatorCategory, OperatorArity,
    DIALECTICAL_NEGATION, DIALECTICAL_CONJUNCTION, AUFHEBUNG,
    CLASSICAL_NEGATION
)

from extensions.temporal_operators import (
    ALWAYS, EVENTUALLY, BECOMING, TEMPORAL_SYNTHESIS
)

from extensions.praxis_operators import (
    PRAXIS_CONDITIONING, PRAXIS_MEDIATION, PRAXIS_TRANSFORMATION
)

# ============================================================================
# 1. REGISTRY STRUCTURE
# ============================================================================

@dataclass
class OperatorRegistry:
    """
    Registry of ALL operator signatures.
    
    Purely structural - knows about operator TYPES,
    not their implementations.
    """
    
    # Main registry
    signatures: Dict[str, OperatorSignature] = field(default_factory=dict)
    
    # Indexes
    by_category: Dict[OperatorCategory, List[OperatorSignature]] = field(default_factory=dict)
    by_arity: Dict[OperatorArity, List[OperatorSignature]] = field(default_factory=dict)
    by_property: Dict[str, List[OperatorSignature]] = field(default_factory=dict)
    
    def __post_init__(self):
        """Initialize with all known operators"""
        self._initialize_registry()
    
    def _initialize_registry(self):
        """Register all operators from all layers"""
        # Core operators
        core_operators = [
            CLASSICAL_NEGATION,
            DIALECTICAL_NEGATION,
            DIALECTICAL_CONJUNCTION,
            AUFHEBUNG
        ]
        
        # Temporal operators
        temporal_operators = [
            ALWAYS,
            EVENTUALLY,
            BECOMING,
            TEMPORAL_SYNTHESIS
        ]
        
        # Praxis operators
        praxis_operators = [
            PRAXIS_CONDITIONING,
            PRAXIS_MEDIATION,
            PRAXIS_TRANSFORMATION
        ]
        
        # Register all
        for op in core_operators + temporal_operators + praxis_operators:
            self.register(op)
    
    def register(self, signature: OperatorSignature):
        """Register a new operator signature"""
        # Create unique key
        key = f"{signature.symbol}_{signature.name}"
        self.signatures[key] = signature
        
        # Index by category
        if signature.category not in self.by_category:
            self.by_category[signature.category] = []
        self.by_category[signature.category].append(signature)
        
        # Index by arity
        if signature.arity not in self.by_arity:
            self.by_arity[signature.arity] = []
        self.by_arity[signature.arity].append(signature)
        
        # Index by properties
        if signature.preserves_contradiction:
            self._add_to_property_index("preserves_contradiction", signature)
        if signature.resolves_contradiction:
            self._add_to_property_index("resolves_contradiction", signature)
    
    def _add_to_property_index(self, property_name: str, signature: OperatorSignature):
        """Add operator to property index"""
        if property_name not in self.by_property:
            self.by_property[property_name] = []
        self.by_property[property_name].append(signature)
    
    # ========================================================================
    # 2. QUERY METHODS
    # ========================================================================
    
    def get_by_symbol(self, symbol: str) -> List[OperatorSignature]:
        """Find operators by symbol (multiple may share symbol)"""
        return [op for op in self.signatures.values() if op.symbol == symbol]
    
    def get_by_name(self, name: str) -> Optional[OperatorSignature]:
        """Get operator by exact name"""
        key = f"_{name}"  # Symbol may vary, name is primary
        for sig in self.signatures.values():
            if sig.name == name:
                return sig
        return None
    
    def get_dialectical_operators(self) -> List[OperatorSignature]:
        """Get all dialectical operators"""
        return self.by_category.get(OperatorCategory.DIALECTICAL, [])
    
    def get_core_dialectical(self) -> List[OperatorSignature]:
        """Get ONLY core dialectical operators (¬ᴰ, ∧ᴰ, ⤊)"""
        core_names = {"dialectical_negation", "dialectical_conjunction", "aufhebung"}
        return [op for op in self.get_dialectical_operators() 
                if op.name in core_names]
    
    def get_temporal_operators(self) -> List[OperatorSignature]:
        """Get operators that are temporal in nature"""
        # Check by symbol (heuristic)
        temporal_symbols = {"□", "◇", "→⃗", "↝"}
        return [op for op in self.signatures.values() 
                if op.symbol in temporal_symbols]
    
    def get_praxis_operators(self) -> List[OperatorSignature]:
        """Get operators that are praxis-dependent"""
        # Check by symbol (heuristic)
        praxis_symbols = {"◉", "↔️", "↻"}
        return [op for op in self.signatures.values() 
                if op.symbol in praxis_symbols]
    
    def get_operators_with_property(self, property_name: str) -> List[OperatorSignature]:
        """Get operators with specific property"""
        return self.by_property.get(property_name, [])
    
    def get_all_operators(self) -> List[OperatorSignature]:
        """Get all registered operators"""
        return list(self.signatures.values())
    
    # ========================================================================
    # 3. RELATION QUERIES
    # ========================================================================
    
    def find_specializations(self, general_op: OperatorSignature) -> List[OperatorSignature]:
        """Find operators that are specializations of given operator"""
        # Heuristic: same symbol but different context
        result = []
        for op in self.signatures.values():
            if (op.symbol == general_op.symbol and 
                op.name != general_op.name and
                op.category == general_op.category):
                result.append(op)
        return result
    
    def find_generalizations(self, specific_op: OperatorSignature) -> List[OperatorSignature]:
        """Find operators that are generalizations of given operator"""
        # Inverse of specializations
        result = []
        for op in self.signatures.values():
            if (op.symbol == specific_op.symbol and 
                op.name != specific_op.name and
                op.category == specific_op.category):
                result.append(op)
        return result
    
    # ========================================================================
    # 4. VALIDATION METHODS
    # ========================================================================
    
    def validate_operator_consistency(self) -> Dict[str, List[str]]:
        """Validate consistency of operator definitions"""
        issues = {
            "duplicate_symbols": [],
            "missing_axioms": [],
            "contradictory_properties": []
        }
        
        # Check for duplicate symbols with different meanings
        symbol_to_names = {}
        for sig in self.signatures.values():
            if sig.symbol in symbol_to_names:
                if sig.name not in symbol_to_names[sig.symbol]:
                    issues["duplicate_symbols"].append(
                        f"Symbol '{sig.symbol}' used for both "
                        f"{symbol_to_names[sig.symbol]} and {sig.name}"
                    )
            else:
                symbol_to_names[sig.symbol] = [sig.name]
        
        # Check for operators with no axioms
        for sig in self.signatures.values():
            if not sig.axioms:
                issues["missing_axioms"].append(
                    f"Operator {sig.name} has no axioms"
                )
        
        # Check for contradictory properties
        for sig in self.signatures.values():
            if (sig.preserves_contradiction and 
                sig.resolves_contradiction):
                issues["contradictory_properties"].append(
                    f"Operator {sig.name} both preserves and resolves contradiction"
                )
        
        return issues
    
    def get_statistics(self) -> Dict[str, int]:
        """Get statistics about registered operators"""
        return {
            "total_operators": len(self.signatures),
            "dialectical": len(self.get_dialectical_operators()),
            "core_dialectical": len(self.get_core_dialectical()),
            "temporal": len(self.get_temporal_operators()),
            "praxis": len(self.get_praxis_operators()),
            "unary": len(self.by_arity.get(OperatorArity.UNARY, [])),
            "binary": len(self.by_arity.get(OperatorArity.BINARY, [])),
        }

# ============================================================================
# 5. GLOBAL REGISTRY INSTANCE
# ============================================================================

# Create global registry instance
GLOBAL_REGISTRY = OperatorRegistry()

# ============================================================================
# 6. EXPORTS
# ============================================================================

__all__ = [
    'OperatorRegistry',
    'GLOBAL_REGISTRY'
]

# ============================================================================
# 7. USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    """Demonstrate registry functionality"""
    
    registry = GLOBAL_REGISTRY
    
    print("=== OPERATOR REGISTRY STATISTICS ===")
    stats = registry.get_statistics()
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    print("\n=== CORE DIALECTICAL OPERATORS ===")
    for op in registry.get_core_dialectical():
        print(f"{op.symbol}: {op.name}")
    
    print("\n=== TEMPORAL OPERATORS ===")
    for op in registry.get_temporal_operators():
        print(f"{op.symbol}: {op.name}")
    
    print("\n=== PRAXIS OPERATORS ===")
    for op in registry.get_praxis_operators():
        print(f"{op.symbol}: {op.name}")
    
    print("\n=== VALIDATION CHECK ===")
    issues = registry.validate_operator_consistency()
    for issue_type, issue_list in issues.items():
        if issue_list:
            print(f"\n{issue_type}:")
            for issue in issue_list:
                print(f"  - {issue}")
        else:
            print(f"\n{issue_type}: None ✓")
