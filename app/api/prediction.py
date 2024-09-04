"""
API module for prediction.

This module contains the endpoints to trigger apartment price
predictions from a pre-trained ML model.

Endpoints:
    - GET /pred/:
        Returns an apartment price prediction based on the
        query inputs provided in the request. The features
        of this query should match the schema in the
        Apartment class.
        Returns HTTP status 400 if the inputs are invalid.

    - POST /pred/:
        Returns an apartment price prediction based on the
        JSON data provided in the body of therequest.
        The request should contain JSON data that matches
        the schema in the  Apartment class.
        Returns HTTP status 400 if the inputs are invalid.
"""

from flask import Blueprint, abort, request
from pydantic import ValidationError

from schema.apartment import Apartment
from services import model_inference_svc

bp = Blueprint('prediction', __name__, url_prefix='/pred')


@bp.get('/')
def get_prediction():
    """
    Retrieve model predictions for the query inputs.

    Returns:
        dict: dictionary containing the prediction
    """
    try:
        apartment_features = Apartment(**request.args)
    except ValidationError:
        abort(code=400, description='Improper input features')  # noqa: WPS432

    prediction = model_inference_svc.predict(
        list(apartment_features.model_dump().values()),
    )

    return {'prediction': prediction}


@bp.post('/')
def post_prediction():
    """
    Retrieve model predictions based on the JSON input query.

    Returns:
        dict: dictionary containing the prediction
    """
    try:
        apartment_features = Apartment(**request.json)
    except ValidationError:
        abort(code=400, description='Improper input features')  # noqa: WPS432

    prediction = model_inference_svc.predict(
        list(apartment_features.model_dump().values()),
    )

    return {'prediction': prediction}
