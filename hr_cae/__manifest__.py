# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "HR CAE",
    "summary": "Employee HR in a CAE - Cooperative Activité Emploi",
    "author": "Coop IT Easy SCRL",
    "website": "https://coopiteasy.be",
    "category": "Human Resources",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["hr", "l10n_fr_department", "hr.recruitment"],
    "data": ["security/ir.model.access.csv", "views/hr.xml", "data/data.xml"],
    "demo": [],
    "installable": True,
    "application": False,
}
