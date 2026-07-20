from app import app, db
from app import Ferret, Pairing, Litter

with app.app_context():

    # Optional: clear existing demo data -- BUT IT HAS TO DELETE WORKING BACKWARD (litter, pairing, parentage, ferret):
    Litter.query.delete()
    Pairing.query.delete()
    
    # Clear self-referencing parent links first:
    for ferret in Ferret.query.all():
        ferret.father_id = None
        ferret.mother_id = None
        
    db.session.commit()
    
    Ferret.query.delete()
    db.session.commit()

    # ----------------
    # Create Ferrets
    # ----------------

    ettin = Ferret(
        breeder_name="NFS",
        name="Ettin",
        sex="hob",
        birth_date="2024-07-15",
        role="breeder",
        status="active",
        proven=True,
        size="standard",
        color="sable",
        pattern="standard",
        fur="natural",
        heritage="domestic",
        temperament="even",
        condition_notes="moderate in every aspect",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    queen_of_hearts = Ferret(
        breeder_name="SAS",
        name="Queen of Hearts",
        sex="jill",
        birth_date="2025-05-11",
        role="breeder",
        status="active",
        proven=False,
        size="standard",
        color="sable",
        pattern="standard",
        fur="plush",
        heritage="domestic",
        temperament="outgoing",
        condition_notes="good structure, proportions, head",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    jabberwocky = Ferret(
        breeder_name="TLFF",
        name="Jabberwocky",
        sex="hob",
        birth_date="2024-05-13",
        role="breeder",
        status="active",
        proven=True,
        size="standard",
        color="albino",
        pattern="standard",
        fur="plush",
        heritage="domestic",
        temperament="goofy",
        condition_notes="",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    enarxi = Ferret(
        breeder_name="DCS",
        name="Enarxi",
        sex="hob",
        birth_date="2023-05-08",
        role="breeder",
        status="active",
        proven=True,
        size="standard",
        color="black sable",
        pattern="standard",
        fur="natural",
        heritage="hybrid 50%",
        temperament="easygoing",
        condition_notes="",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    belles_enchantment = Ferret(
        breeder_name="SAS",
        name="Belle's Enchantment",
        sex="jill",
        birth_date="2025-02-18",
        role="breeder",
        status="active",
        proven=True,
        size="standard",
        color="black sable",
        pattern="standard",
        fur="natural",
        heritage="hybrid",
        temperament="shy",
        condition_notes="smaller than avg.",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    aniko = Ferret(
        breeder_name="",
        name="Aniko",
        sex="jill",
        birth_date="2021-05-14",
        role="breeder",
        status="retired",
        proven=True,
        size="standard",
        color="roan",
        pattern="mitt",
        fur="natural",
        heritage="hybrid",
        temperament="unstable",
        condition_notes="good proportions",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    mr_jingles = Ferret(
        breeder_name="SAS",
        name="Mr. Jingles",
        sex="hob",
        birth_date="2023-07-09",
        role="breeder",
        status="retired",
        proven=True,
        size="standard",
        color="sable",
        pattern="point",
        fur="natural",
        heritage="domestic",
        temperament="easygoing",
        condition_notes="XL",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    princess_pea = Ferret(
        breeder_name="SAS",
        name="Princess Pea",
        sex="jill",
        birth_date="2024-12-14",
        role="breeder",
        status="active",
        proven=True,
        size="mini",
        color="sable",
        pattern="standard",
        fur="natural",
        heritage="domestic",
        temperament="sweet",
        condition_notes="good proportions",
        health_notes="slight head-tilt (mechanical) due to different calcium form in early juvenile development",
        father_id=None,
        mother_id=None
    )

    boggart = Ferret(
        breeder_name="NFS",
        name="Boggart",
        sex="hob",
        birth_date="2024-06-17",
        role="breeder",
        status="active",
        proven=True,
        size="standard",
        color="black sable",
        pattern="standard",
        fur="natural",
        heritage="domestic",
        temperament="high drive",
        condition_notes="stocky, good structure, good proportions",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    gooseberry = Ferret(
        breeder_name="Bajnok",
        name="Gooseberry",
        sex="hob",
        birth_date="2022-03-12",
        role="breeder",
        status="retired",
        proven=True,
        size="mini",
        color="chocolate",
        pattern="standard",
        fur="natural",
        heritage="domestic",
        temperament="busy",
        condition_notes="",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    mother_goose = Ferret(
        breeder_name="SAS",
        name="Mother Goose",
        sex="jill",
        birth_date="2025-04-02",
        role="breeder",
        status="active",
        proven=False,
        size="standard",
        color="roan",
        pattern="mitt",
        fur="natural",
        heritage="domestic",
        temperament="dominant",
        condition_notes="good structure, good proportions",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    swan_maiden = Ferret(
        breeder_name="SHD",
        name="Swan Maiden",
        sex="jill",
        birth_date="2025-05-19",
        role="breeder",
        status="active",
        proven=True,
        size="standard",
        color="sable",
        pattern="standard",
        fur="natural",
        heritage="domestic",
        temperament="reserved",
        condition_notes="good structure, proportions, head",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    rapunzel = Ferret(
        breeder_name="SCF",
        name="Rapunzel",
        sex="jill",
        birth_date="2025-05-01",
        role="breeder",
        status="active",
        proven=False,
        size="mini",
        color="sable",
        pattern="point",
        fur="natural",
        heritage="domestic",
        temperament="reserved",
        condition_notes="",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    queen_titania = Ferret(
        breeder_name="SAS",
        name="Queen Titania",
        sex="jill",
        birth_date="2023-08-06",
        role="breeder",
        status="retired",
        proven=False,
        size="standard",
        color="black sable",
        pattern="standard",
        fur="natural",
        heritage="domestic",
        temperament="reserved",
        condition_notes="smaller than avg. due to poor nutrition wks 1-2",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    cinderella = Ferret(
        breeder_name="SAS",
        name="Cinderella",
        sex="jill",
        birth_date="2023-03-28",
        role="breeder",
        status="retired",
        proven=False,
        size="standard",
        color="roan",
        pattern="mitt",
        fur="natural",
        heritage="hybrid",
        temperament="reserved",
        condition_notes="",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    lady_of_the_lake = Ferret(
        breeder_name="SAS",
        name="Lady of the Lake",
        sex="jill",
        birth_date="2024-04-10",
        role="breeder",
        status="active",
        proven=True,
        size="standard",
        color="black sable",
        pattern="standard",
        fur="natural",
        heritage="hybrid",
        temperament="sweet",
        condition_notes="good structure, proportions",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    avgi = Ferret(
        breeder_name="DCS",
        name="Avgi",
        sex="jill",
        birth_date="2023-05-08",
        role="breeder",
        status="retired",
        proven=True,
        size="standard",
        color="black sable",
        pattern="standard",
        fur="natural",
        heritage="hybrid 50%",
        temperament="sweet",
        condition_notes="good structure, proportions, head",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    suki = Ferret(
        breeder_name="SCF",
        name="Suki",
        sex="jill",
        birth_date="2022-02-15",
        role="breeder",
        status="retired",
        proven=True,
        size="standard",
        color="champagne",
        pattern="standard",
        fur="natural",
        heritage="domestic",
        temperament="reserved",
        condition_notes="good proportions",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    princess_aurora = Ferret(
        breeder_name="SAS",
        name="Princess Aurora",
        sex="jill",
        birth_date="2023-07-09",
        role="breeder",
        status="active",
        proven=True,
        size="mini",
        color="sable",
        pattern="point",
        fur="natural",
        heritage="domestic",
        temperament="sweet",
        condition_notes="good proportions, head",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    selkie = Ferret(
        breeder_name="SAS",
        name="Selkie",
        sex="jill",
        birth_date="2026-02-27",
        role="breeder",
        status="active",
        proven=False,
        size="mini",
        color="black",
        pattern="roan mitt",
        fur="natural",
        heritage="domestic",
        temperament="shy",
        condition_notes="",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    magic_mitten = Ferret(
        breeder_name="SAS",
        name="Magic Mitten",
        sex="hob",
        birth_date="2024-04-10",
        role="breeder",
        status="inactive",
        proven=False,
        size="standard",
        color="black sable",
        pattern="mitt",
        fur="natural",
        heritage="hybrid",
        temperament="friendly",
        condition_notes="good structure, proportions, head",
        health_notes="cryptorchid",
        father_id=None,
        mother_id=None
    )
    
    baba_yaga = Ferret(
        breeder_name="SAS",
        name="Baba Yaga",
        sex="jill",
        birth_date="2024-04-02",
        role="breeder",
        status="active",
        proven=True,
        size="standard",
        color="sable",
        pattern="standard",
        fur="natural",
        heritage="domestic",
        temperament="outgoing",
        condition_notes="",
        health_notes="slight head-tilt (mechanical) due to different calcium form in early juvenile development",
        father_id=None,
        mother_id=None
    )
    
    springtime = Ferret(
        breeder_name="SHD",
        name="Springtime",
        sex="jill",
        birth_date="2022-07-14",
        role="breeder",
        status="retired",
        proven=True,
        size="standard",
        color="sable",
        pattern="point",
        fur="natural",
        heritage="domestic",
        temperament="friendly",
        condition_notes="good structure, proportions, rib cover, head",
        health_notes="",
        father_id=None,
        mother_id=None
    )
        
        
    big_bad_wolf = Ferret(
        breeder_name="SAS",
        name="Big Bad Wolf",
        sex="hob",
        birth_date="2023-07-31",
        role="breeder",
        status="rehomed",
        proven=True,
        size="standard",
        color="roan",
        pattern="mitt",
        fur="natural",
        heritage="hybrid",
        temperament="outgoing",
        condition_notes="good structure, proportions, head",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    genesis = Ferret(
        breeder_name="SHD",
        name="Genesis",
        sex="jill",
        birth_date="2024-05-21",
        role="breeder",
        status="deceased",
        proven=True,
        size="standard",
        color="sable",
        pattern="standard",
        fur="natural",
        heritage="domestic",
        temperament="reserved",
        condition_notes="good structure, proportions, head",
        health_notes="died post-op. tumor removal",
        father_id=None,
        mother_id=None
    )
    
    pied_piper = Ferret(
        breeder_name="SAS",
        name="Pied Piper",
        sex="hob",
        birth_date="2024-04-10",
        role="breeder",
        status="rehomed",
        proven=True,
        size="standard",
        color="black sable",
        pattern="mitt",
        fur="natural",
        heritage="hybrid",
        temperament="dominant",
        condition_notes="stocky, good structure, proportions",
        health_notes="",
        father_id=None,
        mother_id=None
    )
    
    neraida = Ferret(
        breeder_name="",
        name="Neraida",
        sex="jill",
        birth_date="2022-02-17",
        role="breeder",
        status="deceased",
        proven=True,
        size="micro",
        color="sable",
        pattern="standard",
        fur="natural",
        heritage="domestic",
        temperament="friendly",
        condition_notes="",
        health_notes="died of ferret covid, origin unknown",
        father_id=None,
        mother_id=None
    )
    
    steadfast_tin_soldier = Ferret(
        breeder_name="SAS",
        name="Steadfast Tin Soldier",
        sex="hob",
        birth_date="2024-04-02",
        role="breeder",
        status="rehomed",
        proven=True,
        size="standard",
        color="roan",
        pattern="mitt",
        fur="natural",
        heritage="domestic",
        temperament="outgoing",
        condition_notes="good strucutre, head",
        health_notes="",
        father_id=None,
        mother_id=None
    )



    db.session.add_all([
        ettin,
        queen_of_hearts,
        jabberwocky,
        enarxi,
        belles_enchantment,
        aniko,
        mr_jingles,
        princess_pea,
        boggart,
        gooseberry,
        mother_goose,
        swan_maiden,
        rapunzel,
        queen_titania,
        cinderella,
        lady_of_the_lake,
        avgi,
        suki,
        princess_aurora,
        selkie,
        magic_mitten,
        baba_yaga,
        springtime,
        big_bad_wolf,
        genesis,
        pied_piper,
        neraida,
        steadfast_tin_soldier
    ])

    db.session.commit()
    
    # ----------------
    # Add Parentage
    # ----------------
    
    queen_of_hearts.father_id = jabberwocky.id
    queen_of_hearts.mother_id = genesis.id
    
    belles_enchantment.father_id = steadfast_tin_soldier.id
    belles_enchantment.mother_id = avgi.id
    
    mr_jingles.father_id = gooseberry.id
    mr_jingles.mother_id = springtime.id
    
    princess_pea.father_id = gooseberry.id
    princess_pea.mother_id = neraida.id
    
    queen_titania.father_id = gooseberry.id
    queen_titania.mother_id = genesis.id
    
    cinderella.father_id = gooseberry.id
    cinderella.mother_id = aniko.id
    
    lady_of_the_lake.father_id = big_bad_wolf.id
    lady_of_the_lake.mother_id = avgi.id
    
    princess_aurora.father_id = gooseberry.id
    princess_aurora.mother_id = springtime.id
    
    magic_mitten.father_id = enarxi.id
    magic_mitten.mother_id = aniko.id
    
    baba_yaga.father_id = big_bad_wolf.id
    baba_yaga.mother_id = genesis.id
    
    big_bad_wolf.mother_id = aniko.id
    
    pied_piper.father_id = big_bad_wolf.id
    pied_piper.mother_id = avgi.id
    
    db.session.commit()
    
    # ----------------
    # Create Pairings
    # ----------------

    pairing_1 = Pairing(
        jill_id=princess_pea.id,
        hob_id=boggart.id,
        year=2026,
        season="spring",
        compatibility_notes="micro gene development",
        breeding_notes="48hrs",
        planned=False
    )

    pairing_2 = Pairing(
        jill_id=lady_of_the_lake.id,
        hob_id=jabberwocky.id,
        year=2026,
        season="spring",
        compatibility_notes="structure, color question",
        breeding_notes="48hrs",
        planned=False
    )
    
    pairing_3 = Pairing(
        jill_id=swan_maiden.id,
        hob_id=mr_jingles.id,
        year=2026,
        season="spring",
        compatibility_notes="structure",
        breeding_notes="48hrs",
        planned=False
    )
    
    pairing_4 = Pairing(
        jill_id=belles_enchantment.id,
        hob_id=mr_jingles.id,
        year=2026,
        season="spring",
        compatibility_notes="structure, proportion",
        breeding_notes="48hrs",
        planned=False
    )
    
    pairing_5 = Pairing(
        jill_id=mother_goose.id,
        hob_id=ettin.id,
        year=2026,
        season="spring",
        compatibility_notes="proportion",
        breeding_notes="48hrs",
        planned=True
    )
    
    pairing_6 = Pairing(
        jill_id=rapunzel.id,
        hob_id=enarxi.id,
        year=2026,
        season="summer",
        compatibility_notes="micro gene development",
        breeding_notes="24hrs",
        planned=True
    )
    
    pairing_7 = Pairing(
        jill_id=baba_yaga.id,
        hob_id=jabberwocky.id,
        year=2026,
        season="spring",
        compatibility_notes="structure, proportion, heads",
        breeding_notes="48hrs",
        planned=True
    )
    
    pairing_8 = Pairing(
        jill_id=princess_aurora.id,
        hob_id=boggart.id,
        year=2026,
        season="summer",
        compatibility_notes="micro gene development",
        breeding_notes="24hrs",
        planned=True
    )

    db.session.add_all([pairing_1, pairing_2, pairing_3, pairing_4, pairing_5, pairing_6, pairing_7, pairing_8])
    db.session.commit()

    # ----------------
    # Create Litters
    # ----------------

    litter_1 = Litter(
        pairing_id=pairing_1.id,
        year=2026,
        season="spring",
        kits_born=8,
        kits_passed=0,
        kits_survived=8,
        pregnancy_behavior_notes="Nippy during labor",
        birth_notes="Morning birth",
        postpartum_notes=""
    )

    litter_2 = Litter(
        pairing_id=pairing_2.id,
        year=2026,
        season="summer",
        kits_born=7,
        kits_passed=1,
        kits_survived=6,
        pregnancy_behavior_notes="Sleepy 1 day before birth",
        birth_notes="Birth 1 day early",
        postpartum_notes=""
    )

    db.session.add_all([litter_1, litter_2])
    db.session.commit()

    print("Seed data added successfully.")