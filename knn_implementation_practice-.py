from __future__ import annotations

import abc

import collections

import datetime

from math import isclose, hypot

from typing import (

    cast,

    Any,

    Optional,

    Union,

    Iterator,

    Iterable,

    Counter,

    Callable,

    Protocol,

)

import weakref


class Sample:

    """Abstract superclass for all samples."""




    def __init__(

        self,

        sepal_length: float,

        sepal_width: float,

        petal_length: float,

        petal_width: float,

    ) -> None:

        self.sepal_length = sepal_length

        self.sepal_width = sepal_width

        self.petal_length = petal_length

        self.petal_width = petal_width




    def __repr__(self) -> str:

        return (

            f"{self.__class__.__name__}("

            f"sepal_length={self.sepal_length}, "

            f"sepal_width={self.sepal_width}, "

            f"petal_length={self.petal_length}, "

            f"petal_width={self.petal_width}, "

            f")"

        )







class KnownSample(Sample):

    """Abstract superclass for testing and training data, the species is set externally."""




    def __init__(

        self,

        species: str,

        sepal_length: float,

        sepal_width: float,

        petal_length: float,

        petal_width: float,

    ) -> None:

        super().__init__(

            sepal_length=sepal_length,

            sepal_width=sepal_width,

            petal_length=petal_length,

            petal_width=petal_width,

        )

        self.species = species




    def __repr__(self) -> str:

        return (

            f"{self.__class__.__name__}("

            f"sepal_length={self.sepal_length}, "

            f"sepal_width={self.sepal_width}, "

            f"petal_length={self.petal_length}, "

            f"petal_width={self.petal_width}, "

            f"species={self.species!r}, "

            f")"

        )







class TrainingKnownSample(KnownSample):

    """Training data."""




    pass







class TestingKnownSample(KnownSample):

    """Testing data. A classifier can assign a species, which may or may not be correct."""




    def __init__(

        self,

        /,

        species: str,

        sepal_length: float,

        sepal_width: float,

        petal_length: float,

        petal_width: float,

        classification: Optional[str] = None,

    ) -> None:

        super().__init__(

            species=species,

            sepal_length=sepal_length,

            sepal_width=sepal_width,

            petal_length=petal_length,

            petal_width=petal_width,

        )

        self.classification = classification




    def matches(self) -> bool:

        return self.species == self.classification




    def __repr__(self) -> str:

        return (

            f"{self.__class__.__name__}("

            f"sepal_length={self.sepal_length}, "

            f"sepal_width={self.sepal_width}, "

            f"petal_length={self.petal_length}, "

            f"petal_width={self.petal_width}, "

            f"species={self.species!r}, "

            f"classification={self.classification!r}, "

            f")"

        )







class UnknownSample(Sample):

    """A sample provided by a User, not yet classified."""




    pass







class ClassifiedSample(Sample):

    """Created from a sample provided by a User, and the results of classification."""




    def __init__(self, classification: str, sample: UnknownSample) -> None:

        super().__init__(

            sepal_length=sample.sepal_length,

            sepal_width=sample.sepal_width,

            petal_length=sample.petal_length,

            petal_width=sample.petal_width,

        )

        self.classification = classification




    def __repr__(self) -> str:

        return (

            f"{self.__class__.__name__}("

            f"sepal_length={self.sepal_length}, "

            f"sepal_width={self.sepal_width}, "

            f"petal_length={self.petal_length}, "

            f"petal_width={self.petal_width}, "

            f"classification={self.classification!r}, "

            f")"

        
)