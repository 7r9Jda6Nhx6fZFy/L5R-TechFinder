import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)

from werkzeug.exceptions import abort

from techfinder.db import get_db

bp = Blueprint('tech', __name__)


def dict_list_from_row(rows):
    dict_list = []
    d = {}
    for row in rows:
        for key in range(0, len(row)):
            d[row.keys()[key]] = tuple(row)[key]
        dict_list.append(d.copy())
    return dict_list


@bp.route('/')
def index():
    db = get_db()
    techs_rows = db.execute(
        'SELECT id, name, type, category, rank, prerequisite, ring FROM techniques'
    ).fetchall()

    techs = dict_list_from_row(techs_rows)

    return render_template('tech/index.html', techs=techs)


def get_tech(id):
    tech = get_db().execute(
        'SELECT * FROM techniques WHERE id = ?',
        (id,)
    ).fetchone()

    if tech is None:
        abort(404, "Technique id {0} does not exist.".format(id))

    return tech


@bp.route('/<int:id>/detail')
def detail(id):
    tech = get_tech(id)
    return render_template('tech/detail.html', tech=tech)
