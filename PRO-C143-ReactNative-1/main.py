from flask import Flask, jsonify, request

from storage import all_articles, liked_articles, not_liked_articles
from DemographicFiltering import output
from ContentFiltering import get_recommendations

