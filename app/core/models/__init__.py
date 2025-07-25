"""
Core models must be agnostic and not use any external library like `Pydantic` or
`annotated_types`.
Constraints must be defined utilizing `dataclasses.field`, `attr`, `typing`,
etc.
"""
from .base import Base, BaseEmbedded
