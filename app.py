from __future__ import annotations
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select
from marshmallow import ValidationError, fields
from datetime import datetime


# Initialize Flask app
app = Flask(__name__)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
else:
    DB_USER = os.getenv("MYSQL_USER")
    DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
    DB_HOST = os.getenv("MYSQL_HOST")
    DB_NAME = os.getenv("MYSQL_DATABASE")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create Base Model:
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy and Marshamllow:
db = SQLAlchemy(model_class = Base)
db.init_app(app)
ma = Marshmallow(app)



# Models
class Ferret(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Basic Identity for Each Ferret
    breeder_name = db.Column(db.String(200), nullable=True)
    name = db.Column(db.String(200), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    birth_date = db.Column(db.Date)
    
    # Breeding / Program Role
    role = db.Column(db.String(50))
    # examples: breeder, companion
    
    status = db.Column(db.String(50))
    # examples: active, inactive, retired, deceased, rehomed
    
    proven = db.Column(db.Boolean, default=False)
    
    # Genetics / Appearance
    size = db.Column(db.String(50))
    # examples: micro, mini, standard
    
    color = db.Column(db.String(50))
    # examples: albino, black, black sable, champagne, chocolate, cinnamon, DEW, roan, sable
    
    pattern = db.Column(db.String(50))
    # examples: standard, roan mitt, point, solid, white blaze, panda, mitt
    
    fur = db.Column(db.String(50))
    # examples: natural, angora, semi-angora, plush
    
    heritage = db.Column(db.String(50))
    # examples: domestic, polecat, hybrid(50/50)(default), hybrid(%)(manual input)
    
    # Temperament / Condition
    temperament = db.Column(db.Text)
    condition_notes = db.Column(db.Text)
    
    # Health
    health_notes = db.Column(db.Text)
    
    # Parent Relationships
    father_id = db.Column(db.Integer, db.ForeignKey('ferret.id'))
    mother_id = db.Column(db.Integer, db.ForeignKey('ferret.id'))
    
    father = db.relationship('Ferret', remote_side=[id], foreign_keys=[father_id], backref='sired_offspring', post_update=True)
    mother = db.relationship('Ferret', remote_side=[id], foreign_keys=[mother_id], backref='dam_offspring', post_update=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "sex": self.sex,
            "status": self.status,
            "color": self.color
        }
    
    
class Pairing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    year = db.Column(db.Integer)
    season = db.Column(db.String(20))
    
    jill_id = db.Column(db.Integer, db.ForeignKey('ferret.id'), nullable=False)
    hob_id = db.Column(db.Integer, db.ForeignKey('ferret.id'), nullable=False)
    
    jill = db.relationship('Ferret', foreign_keys=[jill_id], backref='pairings_as_jill')
    hob = db.relationship('Ferret', foreign_keys=[hob_id], backref='pairings_as_hob')
    
    compatibility_notes = db.Column(db.Text)
    breeding_notes = db.Column(db.Text)
    planned = db.Column(db.Boolean, default=True)    
    
    def to_dict(self):
        return {
            "id": self.id,
            "jill_id": self.jill_id,
            "hob_id": self.hob_id,
            "year": self.year,
            "season": self.season
        }
    
    
class Litter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   
    pairing_id = db.Column(db.Integer, db.ForeignKey('pairing.id'), nullable=False)
    pairing = db.relationship('Pairing', backref='litters')
   
    year = db.Column(db.Integer, nullable=False)
    season = db.Column(db.String(20), nullable=False)
    birth_date = db.Column(db.Date)
    
    kits_born = db.Column(db.Integer)
    kits_passed = db.Column(db.Integer)
    kits_survived = db.Column(db.Integer)
    
    pregnancy_behavior_notes = db.Column(db.Text)
    birth_notes = db.Column(db.Text)
    postpartum_notes = db.Column(db.Text)    
    
    def to_dict(self):
        return {
            "id": self.id,
            "pairing_id": self.pairing_id,
            "year": self.year,
            "season": self.season,
            "birth_date": self.birth_date,
            "kits_born": self.kits_born,
            "kits_passed": self.kits_passed,
            "kits_survived": self.kits_survived,
            "pregnancy_behavior_notes": self.pregnancy_behavior_notes,
            "birth_notes": self.birth_notes,
            "postpartum_notes": self.postpartum_notes
        }



# Schemas:
class FerretSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model = Ferret
        load_instance = False
        include_fk = True
        
    breeder_name = fields.String(required=False)
    name = fields.String(required=True)
    sex = fields.String(required=True)
    birth_date = fields.Date(required=False)
    
    role = fields.String(required=True)
    status = fields.String(required=True)
    proven = fields.Boolean(required=True)
    
    size = fields.String(required=True)
    color = fields.String(required=True)
    pattern = fields.String(required=True)
    fur = fields.String(required=True)
    heritage = fields.String(required=True)
    
    temperament = fields.String(required=False)
    condition_notes = fields.String(required=False)
    health_notes = fields.String(required=False)
    
    father_id = fields.Integer(required=False)
    mother_id = fields.Integer(required=False)

class PairingSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model = Pairing
        load_instance = False
        include_fk = True
        
    year = fields.Integer(required=True)
    season = fields.String(required=True)
    
    jill_id = fields.Integer(required=True)
    hob_id = fields.Integer(required=True)
    
    compatibility_notes = fields.String(required=False)
    breeding_notes = fields.String(required=False)
    planned = fields.Boolean(required=False)     
        
class LitterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Litter
        load_instance = False
        include_fk = True
        
    pairing_id = fields.Integer(required=True)
    
    year = fields.Integer(required=True)
    season = fields.String(required=True)
    birth_date = fields.Date(required=False)
    
    kits_born = fields.Integer(required=True)
    kits_passed = fields.Integer(required=True)
    kits_survived = fields.Integer(dump_only=True)
    
    pregnancy_behavior_notes = fields.String(required=False)
    birth_notes = fields.String(required=False)
    postpartum_notes = fields.String(required=False)
    
    
# Initialized Schemas:
ferret_schema = FerretSchema()
ferrets_schema = FerretSchema(many=True)

pairing_schema = PairingSchema()
pairings_schema = PairingSchema(many=True)

litter_schema = LitterSchema()
litters_schema = LitterSchema(many=True)

#---------------------
# Home Page
#---------------------

@app.route("/")
def home():
    return render_template("index.html")

#---------------------
# Page Routes
#---------------------

@app.route("/ferrets", methods=['GET', 'POST'])
def ferrets_page():
    
    if request.method == 'POST':
        father_id = request.form.get("father_id")
        mother_id = request.form.get("mother_id")
        
        father_id = int(father_id) if father_id else None
        mother_id = int(mother_id) if mother_id else None
        
        proven_value = request.form.get("proven")
        proven = True if proven_value == "true" else False
        
        new_ferret = Ferret(
            breeder_name=request.form.get("breeder_name"),
            name=request.form.get("name"),
            sex=request.form.get("sex"),
            birth_date=request.form.get("brith_date") or None,
            role=request.form.get("role"),
            status=request.form.get("status"),
            proven=proven,
            size=request.form.get("size"),
            color=request.form.get("color"),
            pattern=request.form.get("pattern"),
            fur=request.form.get("fur"),
            heritage=request.form.get("heritage"),
            temperament=request.form.get("temperament"),
            condition_notes=request.form.get("condition_notes"),
            health_notes=request.form.get("health_notes"),
            father_id=father_id,
            mother_id=mother_id
        )
        
        db.session.add(new_ferret)
        db.session.commit()
        
        return redirect("/ferrets")
    
 # Ask SQLAlchemy to give me ALL ferret records from the database:   
    ferrets = Ferret.query.all()
 # Send ALL ferret records to the Jinja template:   
    return render_template("ferrets.html", ferrets=ferrets)

@app.route("/ferrets/<int:ferret_id>/edit", methods=['GET', 'POST'])
def edit_ferret(ferret_id):
    ferret = Ferret.query.get_or_404(ferret_id)
    ferrets = Ferret.query.all()
    
    if request.method == 'POST':
        ferret.breeder_name = request.form["breeder_name"]
        ferret.name = request.form["name"]
        ferret.sex = request.form["sex"]
        ferret.role = request.form["role"]
        ferret.status = request.form["status"]
        ferret.proven = request.form["proven"].lower() == "true"
        ferret.size = request.form["size"]
        ferret.color = request.form["color"]
        ferret.pattern = request.form["pattern"]
        ferret.fur = request.form["fur"]
        ferret.heritage = request.form["heritage"]
        ferret.temperament = request.form["temperament"]
        ferret.condition_notes = request.form["condition_notes"]
        ferret.health_notes = request.form["health_notes"]
        ferret.father_id = int(request.form["father_id"]) if request.form["father_id"] else None
        ferret.mother_id = int(request.form["mother_id"]) if request.form["mother_id"] else None
        
        db.session.commit()
        return redirect(url_for("ferrets_page"))
    
    return render_template("edit_ferret.html", ferret=ferret, ferrets=ferrets)

@app.route("/ferrets/<int:ferret_id>/delete", methods=['POST'])
def delete_ferret_from_page(ferret_id):
    ferret = db.session.get(Ferret, ferret_id)
    
    if not ferret:
        return redirect("/ferrets")
    
    db.session.delete(ferret)
    db.session.commit()
    
    return redirect("/ferrets")

@app.route("/pairings", methods=['GET', 'POST'])
def pairings_page():
    current_year = datetime.now().year
    years = range(current_year - 50, current_year + 6)
    
    if request.method == 'POST':
        jill_id = request.form.get("jill_id")
        hob_id = request.form.get("hob_id")
        
        jill_id = int(jill_id) if jill_id else None
        hob_id = int(hob_id) if hob_id else None
        
        planned = request.form.get("planned") == "planned"
        
        add_pairing = Pairing(
            year=request.form.get("year"),
            season=request.form.get("season"),
            jill_id=jill_id,
            hob_id=hob_id,
            compatibility_notes=request.form.get("compatibility_notes"),
            breeding_notes=request.form.get("breeding_notes"),
            planned=planned
        )
        
        db.session.add(add_pairing)
        db.session.commit()
        
        return redirect("/pairings")
    
    pairings = Pairing.query.all()
    jills = Ferret.query.filter_by(sex="jill").all()
    hobs = Ferret.query.filter_by(sex="hob").all()

    return render_template("pairings.html", years=years, current_year=current_year, pairings=pairings, jills=jills, hobs=hobs)

@app.route("/pairings/<int:pairing_id>/edit", methods=['GET', 'POST'])
def edit_pairing(pairing_id):
    pairing = Pairing.query.get_or_404(pairing_id)
    
    current_year = datetime.now().year
    years = range(current_year - 50, current_year + 6)
    
    jills = Ferret.query.filter_by(sex="jill").all()
    hobs = Ferret.query.filter_by(sex="hob").all()
    
    if request.method == 'POST':
        pairing.year = int(request.form["year"])
        pairing.season = request.form["season"]
        pairing.jill_id = int(request.form["jill_id"])
        pairing.hob_id = int(request.form["hob_id"])
        pairing.compatibility_notes = request.form["compatibility_notes"]
        pairing.breeding_notes = request.form["breeding_notes"]
        pairing.planned = request.form["planned"] == "planned"
        
        db.session.commit()
        return redirect(url_for("pairings_page"))
    
    return render_template("edit_pairing.html", pairing=pairing, years=years, current_year=current_year, jills=jills, hobs=hobs)
   
@app.route("/pairings/<int:pairing_id>/delete", methods=['POST'])
def delete_pairing_from_page(pairing_id):
    pairing = Pairing.query.get_or_404(pairing_id)
    
    db.session.delete(pairing)
    db.session.commit()
    
    return redirect(url_for("pairings_page"))



@app.route("/litters", methods=['GET', 'POST'])
def litters_page():
    current_year = datetime.now().year
    years = range(current_year - 50, current_year + 6)
    
    if request.method == 'POST':
        kits_born = int(request.form["kits_born"])
        kits_passed = int(request.form["kits_passed"])
        kits_survived = kits_born - kits_passed
        
        add_litter = Litter(
            pairing_id=int(request.form.get("pairing_id")),
            year=int(request.form.get("year")),
            season=request.form.get("season"),
            birth_date=request.form.get("birth_date") or None,
            kits_born=kits_born,
            kits_passed=kits_passed,
            kits_survived=kits_survived,
            pregnancy_behavior_notes=request.form.get("pregnancy_behavior_notes"),
            birth_notes=request.form.get("birth_notes"),
            postpartum_notes=request.form.get("postpartum_notes")
        )
        
        db.session.add(add_litter)
        db.session.commit()
        
        return redirect(url_for("litters_page"))
    
    litters = Litter.query.all()
    pairings = Pairing.query.all()

    return render_template("litters.html", litters=litters, pairings=pairings, years=years, current_year=current_year)


@app.route("/litters/<int:litter_id>/edit", methods=['GET', 'POST'])
def edit_litter(litter_id):
    litter = Litter.query.get_or_404(litter_id)
    
    current_year = datetime.now().year
    years = range(current_year - 50, current_year + 6)
    pairings = Pairing.query.all()
    
    if request.method == 'POST':
        kits_born = int(request.form["kits_born"])
        kits_passed = int(request.form["kits_passed"])
        kits_survived = kits_born - kits_passed
        
        litter.year = int(request.form["year"])
        litter.season = request.form["season"]
        litter.pairing_id = int(request.form["pairing_id"])
        litter.birth_date = request.form["birth_date"] or None
        litter.kits_born = kits_born
        litter.kits_passed = kits_passed
        litter.kits_survived = kits_survived
        litter.pregnancy_behavior_notes = request.form["pregnancy_behavior_notes"]
        litter.birth_notes = request.form["birth_notes"]
        litter.postpartum_notes = request.form["postpartum_notes"]
        
        db.session.commit()
        return redirect(url_for("litters_page"))
    
    return render_template("edit_litter.html", litter=litter, years=years, current_year=current_year, pairings=pairings)


@app.route("/litters/<int:litter_id>/delete", methods=['POST'])
def delete_litter_from_page(litter_id):
    litter = Litter.query.get_or_404(litter_id)
    
    db.session.delete(litter)
    db.session.commit()
    
    return redirect(url_for("litters_page"))


@app.route("/reports", methods=['GET', 'POST'])
@app.route("/reports/", methods=['GET', 'POST'])
def reports_page():
    report_type = None
    report_data = []
    selected_year = None
    
    if request.method == "POST":
        report_type = request.form.get("report_type")
        selected_year = request.form.get("year")
        
        if report_type == "litters_by_year":
            report_data = Litter.query.filter_by(year=selected_year).all()
            
        elif report_type == "resident_ferrets":
            report_data = Ferret.query.filter(
                Ferret.status.in_(["active", "inactive", "retired"])
            ).order_by(Ferret.status, Ferret.name).all()
            
        elif report_type == "pairing_history":
            report_data = Pairing.query.all()
            
    return render_template(
        "reports.html",
        report_type=report_type,
        report_data=report_data,
        selected_year=selected_year
    )


#------------------CRUD ENDPOINTS----------------------------

# GET All Ferrets
@app.route('/api/ferrets', methods=['GET'])
def get_ferrets():
    query = select(Ferret)
    ferrets = db.session.execute(query).scalars().all()
        
    return ferrets_schema.jsonify(ferrets), 200    

# GET One Ferret
@app.route('/ferret/<int:id>', methods=['GET'])
def get_ferret(id):
    
    ferret = db.session.get(Ferret, id)
    
    if not ferret:
        return jsonify({"message": "Invalid ferret ID"}), 404
    
    return ferret_schema.jsonify(ferret), 200

# POST (add) a Ferret    
@app.route('/add-ferret', methods=['POST'])
def add_ferret():
    
    data = request.json

    proven = data.get("proven")

    new_ferret = Ferret(
        name=data.get("name"),
        breeder_name=data.get("breeder_name"),
        birth_date=data.get("birth_date"),
        sex=data.get("sex"),
        role=data.get("role"),
        status=data.get("status"),
        proven=proven,
        size=data.get("size"),
        color=data.get("color"),
        pattern=data.get("pattern"),
        fur=data.get("fur"),
        heritage=data.get("heritage"),
        temperament=data.get("temperament"),
        condition_notes=data.get("condition_notes")
    )

    db.session.add(new_ferret)
    db.session.commit()

    return ferret_schema.jsonify(new_ferret), 201


# PUT (update) a Ferret
@app.route('/ferret/<int:id>', methods=['PUT'])
def update_ferret(id):
    ferret = db.session.get(Ferret, id)
    
    if not ferret:
        return jsonify({"message": "Invalid ferret ID"}), 404
    
    try: 
        ferret_data = ferret_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    ferret.name = ferret_data['name']
    ferret.breeder_name = ferret_data['breeder_name']
    ferret.birth_date = ferret_data['birth_date']
    ferret.sex = ferret_data['sex']
    ferret.role = ferret_data['role']
    ferret.status = ferret_data['status']
    ferret.proven = ferret_data['proven']
    ferret.size = ferret_data['size']
    ferret.color = ferret_data['color']
    ferret.pattern = ferret_data['pattern']
    ferret.fur = ferret_data['fur']
    ferret.heritage = ferret_data['heritage']
    ferret.temperament = ferret_data['temperament']
    ferret.condition_notes = ferret_data['condition_notes']
    
    db.session.commit()
    return ferret_schema.jsonify(ferret), 200

# DELETE a Ferret
@app.route('/ferret/<int:id>', methods=['DELETE'])
def delete_ferret(id):
    ferret = db.session.get(Ferret, id)
    
    if not ferret:
        return jsonify({"message": "Invalid ferret ID"}), 404
    
    db.session.delete(ferret)
    db.session.commit()
    return jsonify({"message": f"successfully deleted ferret {id}"}), 200

#---------------------------------------------------------------

# GET All Pairings
@app.route('/api/pairings', methods=['GET'])
def get_pairings():
    query = select(Pairing)
    pairings = db.session.execute(query).scalars().all()
    
    return pairings_schema.jsonify(pairings), 200

# GET One Pairing
@app.route('/pairing/<int:id>', methods=['GET'])
def get_pairing(id):
    
    pairing = db.session.get(Pairing, id)
    
    if not pairing:
        return jsonify({"message": "Invalid pairing ID"}), 404
    
    return pairing_schema.jsonify(pairing), 200

# POST (create) a Pairing
@app.route('/add-pairing', methods=['POST'])
def add_pairing():
    
        data = request.json

        planned = data.get("planned")

        new_pairing = Pairing(
            year=int(data.get("year")),
            season=data.get("season"),
            jill_id=int(data.get("jill_id")),
            hob_id=int(data.get("hob_id")),
            compatibility_notes=data.get("compatibility_notes"),
            breeding_notes=data.get("breeding_notes"),
            planned=planned
        )

        db.session.add(new_pairing)
        db.session.commit()

        return pairing_schema.jsonify(new_pairing), 201


# PUT (update) a Pairing
@app.route('/pairing/<int:id>', methods=['PUT'])
def update_pairing(id):
    pairing = db.session.get(Pairing, id)
    
    if not pairing:
        return jsonify({"message": "Invalid pairing ID"}), 404
    
    try: 
        pairing_data = pairing_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    pairing.year = pairing_data['year']
    pairing.season = pairing_data['season']
    pairing.jill_id = pairing_data['jill_id']
    pairing.hob_id = pairing_data['hob_id']
    pairing.compatibility_notes = pairing_data['compatibility_notes']
    pairing.breeding_notes = pairing_data['breeding_notes']
    pairing.planned = pairing_data['planned']
    
    db.session.commit()
    return pairing_schema.jsonify(pairing), 200

# DELETE a Pairing
@app.route('/pairing/<int:id>', methods=['DELETE'])
def delete_pairing(id):
    pairing = db.session.get(Pairing, id)
    
    if not pairing:
        return jsonify({"message": "Invalid pairing ID"}), 404
    
    db.session.delete(pairing)
    db.session.commit()
    return jsonify({"message": f"successfully deleted pairing {id}"}), 200

#---------------------------------------------------------------

# GET All Litters
@app.route('/api/litters', methods=['GET'])
def get_litters():
    query = select(Litter)
    litters = db.session.execute(query).scalars().all()
    
    return litters_schema.jsonify(litters), 200

# GET One Litter
@app.route('/litter/<int:id>', methods=['GET'])
def get_litter(id):
    
    litter = db.session.get(Litter, id)
    
    if not litter:
        return jsonify({"message": "Invalid litter ID"}), 404
    
    return litter_schema.jsonify(litter), 200

# Add a Litter
@app.route('/add-litter', methods=['POST'])
def add_litter():
    
    data = request.json

    kits_born = data.get("kits_born")
    kits_passed = data.get("kits_passed")

    new_litter = Litter(
        pairing_id=int(data.get("pairing_id")),
        year=int(data.get("year")),
        season=data.get("season"),
        birth_date=data.get("birth_date"),
        kits_born=kits_born,
        kits_passed=kits_passed,
        kits_survived=kits_born - kits_passed,
        pregnancy_behavior_notes=data.get("pregnancy_behavior_notes"),
        birth_notes=data.get("birth_notes"),
        postpartum_notes=data.get("postpartum_notes")
    )

    db.session.add(new_litter)
    db.session.commit()

    return litter_schema.jsonify(new_litter), 201

# PUT (update) a Litter
@app.route('/litter/<int:id>', methods=['PUT'])
def update_litter(id):
    litter = db.session.get(Litter, id)
    
    if not litter:
        return jsonify({"message": "Invalid litter ID"}), 404
    
    try: 
        litter_data = litter_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    litter.year = litter_data['year']
    litter.season = litter_data['season']
    litter.birth_date = litter_data['birth_date']
    litter.kits_born = litter_data['kits_born']
    litter.kits_passed = litter_data['kits_passed']
    litter.kits_survived = (litter.kits_born - litter.kits_passed)
    litter.pregnancy_behavior_notes = litter_data['pregnancy_behavior_notes']
    litter.birth_notes = litter_data['birth_notes']
    litter.postpartum_notes = litter_data['postpartum_notes']
    
    db.session.commit()
    return litter_schema.jsonify(litter), 200

# DELETE a litter
@app.route('/litter/<int:id>', methods=['DELETE'])
def delete_litter(id):
    litter = db.session.get(Litter, id)
    
    if not litter:
        return jsonify({"message": "Invalid litter ID"}), 404
    
    db.session.delete(litter)
    db.session.commit()
    return jsonify({"message": f"successfully deleted litter {id}"}), 200

#--------------------------------------------------------------------------------------
# Queries ------------------------

@app.route("/jill/<int:jill_id>/litters", methods=['GET'])
def get_litters_for_jill(jill_id):
    litters = (Litter.query.join(Pairing).filter(Pairing.jill_id == jill_id).all())
    
    return jsonify([litter.to_dict() for litter in litters])


@app.route("/hob/<int:hob_id>/jills", methods=['GET'])
def get_jills_for_hob(hob_id):
    jills = (Ferret.query.join(Pairing, Ferret.id == Pairing.jill_id).filter(Pairing.hob_id == hob_id).all())
    
    return jsonify([jill.to_dict() for jill in jills])


@app.route("/year/<int:year>/litters", methods=['GET'])
def get_litters_by_year(year):
    litters = (Litter.query.filter(Litter.year == year).all())
    
    return jsonify([litter.to_dict() for litter in litters])


@app.route("/breeders/active", methods=['GET'])
def get_active_breeders():
    active_breeders = (Ferret.query.filter(Ferret.status == "active").all())
    
    return jsonify([ferret.to_dict() for ferret in active_breeders])


@app.route("/breeders/retired", methods=['GET'])
def get_retired_breeders():
    retired_breeders = (Ferret.query.filter(Ferret.status == "retired").all())
    
    return jsonify([ferret.to_dict() for ferret in retired_breeders])


@app.route("/year/<int:year>/summary", methods=['GET'])
def get_year_summary(year):
    litters = (Litter.query.filter(Litter.year == year).all())
    
    total_litters = len(litters)
    
    total_kits_born = sum(litter.kits_born or 0 for litter in litters)
    total_kits_passed = sum(litter.kits_passed or 0 for litter in litters)
    total_kits_survived = sum(litter.kits_survived or 0 for litter in litters)
    
    if total_kits_born > 0:
        survival_rate = total_kits_survived / total_kits_born
    else:
        survival_rate = 0
        
    return jsonify({"year": year, "total_litters": total_litters, "total_kits_born": total_kits_born, "total_kits_survived": total_kits_survived, "total_kits_passed": total_kits_passed, "survival_rate": survival_rate})


@app.route("/hob/<int:hob_id>/production-summary", methods=['GET'])
def get_hob_summary(hob_id):
    pairings = Pairing.query.filter(Pairing.hob_id == hob_id).all()
    
    pairing_ids = [pairing.id for pairing in pairings]
    
    litters = Litter.query.filter(Litter.pairing_id.in_(pairing_ids)).all()
    
    total_litters = len(litters)
    
    total_kits_born = sum(litter.kits_born or 0 for litter in litters)
    
    total_kits_survived = sum(litter.kits_survived or 0 for litter in litters)
    
    average_litter_size = total_kits_born / total_litters if total_litters > 0 else 0
    
    return jsonify({"hob_id": hob_id, "total_pairings": len(pairings), "total_litters": total_litters, "total_kits_born": total_kits_born, "total_kits_survived": total_kits_survived, "average_litter_size": average_litter_size})


@app.route("/jill/<int:jill_id>/production-summary", methods=['GET'])
def get_jill_summary(jill_id):
    pairings = Pairing.query.filter(Pairing.jill_id == jill_id).all()
    
    pairing_ids = [pairing.id for pairing in pairings]
    
    litters = Litter.query.filter(Litter.pairing_id.in_(pairing_ids)).all()
    
    total_litters = len(litters)
    
    total_kits_born = sum(litter.kits_born or 0 for litter in litters)
    
    total_kits_survived = sum(litter.kits_survived or 0 for litter in litters)
    
    average_litter_size = total_kits_born / total_litters if total_litters > 0 else 0
    
    return jsonify({"jill_id": jill_id, "total_pairings": len(pairings), "total_litters": total_litters, "total_kits_born": total_kits_born, "total_kits_survived": total_kits_survived, "average_litter_size": average_litter_size})





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)