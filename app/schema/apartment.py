"""Schema for apartment input."""

from pydantic import BaseModel


class Apartment(BaseModel):
    """
    Apartment schema.

    Schema used for model inputs during inference.

    Attributes:
        area: Apartment area
        construction_year: Year of construction
        bedrooms: number of bedrooms
        garden: area (m^2) of garden
        balcony_yes: 1 if has balcony, 0 otherwise
        parking_yes: 1 if has parking, 0 otherwise
        furnished_yes: 1 if furnished, 0 otherwise
        garage_yes: 1 if has garage, 0 otherwise
        storage_yes: 1 if has storage unit, 0 otherwise
    """

    area: int
    construction_year: int
    bedrooms: int
    garden: int
    balcony_yes: int
    parking_yes: int
    furnished_yes: int
    garage_yes: int
    storage_yes: int
