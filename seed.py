import csv
import json
from database import db

from models import *


def users():
    fem_names = ['Aabha','Aaliyah','Aalt','Aaltje','Aanandini','Aba','Ababuo','Abagbe','Abam','Abame','Abana','Abarrane','Abayomi','Abbie','Abby','Abebi','Abedabun','Abeke','Abelia','Abella','Abelle','Abellona','Abena','Abeo','Abequa','Abey','Abeytu','Abeytzi','Abha','Abhaa','Abi','Abia','Abida','Abidemi','Abigail','Abimbola','Abinkanile','Abiona','Abir','Abmaba','Abra','Acacia','Acadia','Acaija','Acantha','Accalia','Aceline','Acenith','Achala','Achalaa','Achsa','Achsah','Acima','Ada','Adah','Adalheid','Adalheidis','Adalia','Adaliah','Adalina','Adamina','Adamma','Adan','Adanna','Adar','Adara','Addalah','Addiah','Addie','Addula','Ade','Adebola','Adedagbo','Adelaide','Adele','Adeleke','Adelind','Adelinda','Adeline','Adella','Adelpha','Adena','Adeola','Aderes','Aderet','Adesimbo','Adesina','Adhika','Adhita','Adia','Adiba','Adiella','Adila','Adilah','Adima','Adin','Adina','Adinah','Adine','Adira','Adiran','Aditi','Adiva','Adlai','Admete','Adola','Adolpha','Adoncia','Adonia','Adora','Adorabelle','Adoree','Adoria','Adorna','Adowa','Adra','Adrastea','Adrea','Adria','Adriah','Adrian','Adriana','Adriane','Adrianna','Adriannah','Adriano','Adrie','Adriena','Adrienne','Adryan','Adsila','Aduke','Aida','Aimee','Aisha','Alaina','Alana','Alanis','Alannah','Alberta','Aleida','Alessa','Alessandra','Alexa','Alexandra','Alfreda','Alice','Alicia','Alida','Aline','Alisha','Alyosha','Alyssa','Amanda','Amber','Amelia','Amy','Anada','Andrea','Andreia','Andrina','Angela','Angelina','Angie','Aniela','Anila','Ann','Anna','Annabel','Annabelle','Annie','Antoinette','Antonia','Antonina','Anuja','Anya','April','Ardala','Arlene','Augustina','Ava','Avichayil','Avigail','Avijah','Avira','Avital','Beatrice','Belinda','Benita','Bertha','Beth','Bethan','Bethany','Bonnie','Brenda','Brenna','Briana','Brianna','Bronislava','Brooke','Bryany','Bryna','Cacia','Caitlin','Cara','Carla','Carlene','Carly','Carrie','Casey','Casia','Cassie','Catherine','Celina','Cerys','Charlene','Charley','Charlize','Charlotte','Chelsea','Chloe','Christel','Christina','Christine','Clara','Claudette','Cleva','Connie','Cosima','Cosma','Courtney','Cristina','Cristine','Crystal','Daisy','Dalina','Daline','Damiana','Danette','Daniela','Danielle','Danita','Darcy','Davida','Davina','Dayna','Deanna','Deborah','Deeanna','Del','Delina','Della','Delly','Delyne','Demi','Denisa','Denise','Dericka','Diana','Dina','Djamila','Dola','Donalda','Doncia','Donella','Donna','Dora','Dori','Dory','Ebony','Edelie','Edeline','Eden','Edith','Edwarda','Eleanor','Elena','Elfreda','Eline','Elise','Eliza','Elizabeth','Ella','Ellen','Ellie','Eloise','Elsie','Elvina','Emelie','Emilia','Emily','Emma','Emmanuella','Emmanuelle','Erin','Erna','Esme','Estebana','Esther','Etta','Eugina','Eva','Eve','Evelyn','Evie','Faith','Fannie','Farzaneh','Fatima','Faustina','Faustine','Faye','Fedora','Fernanda','Ffion','Fifi','Filippa','Florence','Frances','Francesca','Freda','Fredrica','Fredrika','Freya','Gabriella','Gabrielle','Gael','Gail','Genie','Georgia','Georgina','Geraldine','Giulia','Grace','Guillelmina','Hadria','Hadrian','Hadrienne','Hannah','Harriet','Hasna','Hattie','Hazel','Heather','Heidi','Hella','Hennie','Henrietta','Henrika','Hollie','Holly','Imogen','India','Isabel','Isabella','Isabelle','Isla','Isobel','Jade','Jaime','Jakoba','Jamesina','Jamia','Jamie','Jamilyn','Janey','Janie','Jasmine','Jemima','Jenna','Jennifer','Jerica','Jessica','Jessie','Jetta','Jo','Joel','Josephe','Josephine','Joy','Juana','Jude','Judith','Judy','Julia','Juliana','Justeen','Justeene','Justine','Justyne','Kate','Katherine','Kathleen','Kathryn','Katie','Kayla','Kayleigh','Keira','Keitha','Kelly','Kelsey','Kevia','Khalila','Kiera','Kirsti','Klaudie','Kristina','Kristy','Lady','Lara','Latoya','Laura','Lauren','Laurie','Layla','Leah','Lena','Leona','Leondra','Leondrea','Leonela','Libby','Lillian','Lillie','Lilly','Lily','Lina','Linda','Lisa','Lois','Lola','Lottie','Louella','Louise','Lovisa','Lucy','Lulu','Lydia','Maddison','Madeleine','Madison','Mae','Maisie','Marcelina','Marcia','Marcie','Margaret','Margie','Maria','Marie','Martha','Martina','Marva','Marvina','Mary','Maryam','Mathilda','Mathilde','Matilda','Matilde','Maurisa','Maxima','Maxine','Maya','Megan','Melissa','Mia','Michaela','Michelle','Miliana','Millie','Mina','Mollie','Molly','Morgan','Nancy','Nannie','Naomi','Natalie','Natasha','Nelly','Niamh','Nicia','Nicola','Nicole','Nicoletta','Nicolette','Nigella','Nikol','Nikolett','Nikolia','Norma','Olivia','Paige','Patricia','Paula','Paulina','Pauline','Pavlina','Peta','Petra','Petrina','Philippa','Phoebe','Poppy','Posy','Rachel','Rebecca','Rhonda','Rihanna','Roberta','Robyn','Rosa','Rose','Rosie','Ruby','Ruth','Ryana','Ryanne','Sadie','Samantha','Sandra','Sara','Sarah','Savannah','Scarlett','Sebastia','Shannon','Sharlene','Shawna','Simone','Skye','Sofia','Sophia','Sophie','Stella','Steph','Stephanie','Stephie','Stina','Sue','Summer','Tam','Tammy','Tara','Taura','Taylor','Tegan','Teresa','Thea','Theodora','Thomasina','Thyra','Tia','Tiffany','Tilly','Tommy','Toni','Toya','Traci','Tyler','Vanessa','Vasilisa','Velma','Victoria','Victorine','Vitoria','Wilhelmina','Willie','Wilma','Yaroslava','Yasmin','Zahra','Zainab','Zandra','Zara','Zlata','Zlatica','Zoe']  
    masc_names = ['Aadi','Aaditva','Aakav','Aakesh','Aakil','Aalok','Aamin','Aanan','Aandaleeb','Aaron','Aatmadeva','Aatmik','Ab','Abad','Abarran','Abayomi','Abba','Abbas','Abbe','Abbey','Abbott','Abby','Abda','Abdel','Abdul','Abdullah','Abe','Abeeku','Abejide','Abel','Abelard','Abey','Abhiraja','Abia','Abid','Abie','Abija','Abijah','Abiodun','Abiola','Abir','Abishai','Able','Abna','Abnar','Abner','Abnor','Abornazine','Abraham','Abrahamo','Abrahan','Abram','Abrami','Abramo','Abran','Absalom','Absolon','Ace','Acer','Acestes','Achaius','Acharon','Achates','Achav','Achazia','Achaziah','Achazya','Achazyahu','Achban','Achelous','Acher','Acheron','Achida','Achill','Achille','Achillea','Achilles','Achim','Achimelech','Achisar','Achishar','Achiya','Achiyahu','Acie','Acim','Ackerleigh','Ackerley','Ackleigh','Ackley','Actaeon','Acton','Ad','Adad','Adael','Adaia','Adaiah','Adair','Adal','Adalar','Adalard','Adalfieri','Adalric','Adam','Adamnan','Adamo','Adams','Adamya','Adan','Adao','Adapa','Adar','Adare','Adaya','Addae','Addam','Addie','Addis','Addison','Addy','Ade','Adebayo','Adeben','Adejola','Adel','Adelar','Adelard','Adelric','Adesola','Adhamh','Adhamhnan','Adheesha','Adhideva','Adib','Adiel','Adika','Adil','Adin','Adio','Adir','Adiran','Adisa','Adisson','Aditsan','Aditya','Adiv','Adlai','Adlar','Adler','Adley','Admon','Adnah','Adnan','Adnet','Adney','Adnot','Adoeete','Adoerte','Adofo','Adolfo','Adolfus','Adolph','Adolphe','Adom','Adon','Adonia','Adoniah','Adonijah','Adonis','Adoniya','Adoniyah','Adooeette','Adrea','Adri','Adria','Adrian','Adriana','Adriane','Adriano','Adrie','Adriel','Adryan','Adunbi','Adusa','Adwele','Ahab','Aharon','Ahaziah','Ahaziahu','Ahia','Ahiah','Ahimelech','Ahishar','Ahmed','Akil','Akilles','Alan','Albert','Alex','Alexander','Alfred','Alvin','Andrew','Angelo','Angelus','Anil','Anthony','Anton','Anuj','Archie','Ardal','Ari','Arin','Arlen','Arny','Arthur','Augustus','Austin','Aviah','Avida','Aviel','Avimelech','Avisha','Avner','Avram','Avrom','Barrie','Barry','Ben','Benito','Benjamin','Bob','Bobby','Bornbazine','Bradley','Bram','Brandan','Brandon','Brendan','Brian','Bronislaw','Brooke','Bryan','Burt','Caleb','Callum','Carl','Casey','Charles','Charley','Charlie','Christian','Christophe','Christopher','Claude','Claudius','Cliff','Cole','Connor','Conor','Cosmo','Craig','Cristiano','Curtis','Damian','Daniel','Danny','David','Dean','Declan','Del','Denis','Dennis','Derek','Dewey','Dolph','Dolphus','Dominic','Donald','Douglas','Eb','Ebby','Ebner','Ebony','Eddie','Eden','Edward','Edwin','Emil','Emiliano','Emmanuel','Eric','Erin','Ernest','Esteban','Ethan','Euan','Eugene','Ewan','Faith','Farzan','Faust','Faustino','Fernando','Frances','Frank','Fraser','Fred','Freddie','Frederick','Garfield','Gary','Garyn','George','Georgie','Gerald','Gregory','Grover','Hadria','Hadrian','Hadrienne','Hamza','Haroun','Harrison','Harry','Harvey','Hassan','Helge','Henry','Homer','Hugh','Hugo','Ibrahim','Isaac','Islay','Jack','Jackson','Jacob','Jade','Jaime','Jaimi','Jake','Jakob','James','Jamie','Jamil','Jared','Jason','Jasper','Jenkins','Jeremy','Jessie','Jim','Jimi','Jimmy','Jo','Joe','Joel','John','Johnny','Jonathan','Joseph','Josh','Joshua','Juan','Judah','Julio','Julius','Justin','Keith','Kelly','Kelsey','Kenneth','Kevin','Khalil','Kyle','Lara','Lawrence','Leo','Leon','Leonard','Leonardo','Lewis','Liam','Lloyd','Louis','Lucas','Luis','Luke','Maddison','Madison','Marc','Marcello','Marcus','Mario','Mark','Martin','Martine','Marvin','Matt','Matthew','Maurice','Max','Maximilian','Maximus','Maxwell','Melvin','Michael','Mike','Miles','Mitchell','Mohamed','Mohammad','Mohammed','Morgan','Muhammad','Muhammed','Myles','Nathan','Nathaniel','Neil','Nicholas','Nick','Nicolas','Nigel','Noah','Norman','Oliver','Omar','Oscar','Owen','Patrick','Paul','Peter','Philip','Phillip','Ralph','Raymond','Reuben','Rhys','Richard','Robert','Robyn','Ron','Ronnie','Roosevelt','Roy','Russell','Ryan','Samuel','Sara','Scott','Sean','Sebastian','Seth','Shannon','Simon','Sonny','Sophus','Stanley','Stephen','Steve','Steven','Stevie','Taurus','Taylor','Tegan','Terika','Theo','Theodore','Thomas','Timothy','Tobias','Tom','Tommy','Tony','Travis','Tristan','Tyler','Tyr','Vasiliy','Victor','Vincent','Walter','Warren','Wilhelm','Will','William','Willie','Yaroslav','Yusuf','Zac','Zachary','Zack','Zak','Zlatan']
    all_names = fem_names + masc_names
    created_count = 0
    db.session.begin()

    try:
        for name in all_names:
            user = User(
                name=name,
            )
            db.session.add(user)
            db.session.commit()
            created_count += 1
    except:
        db.session.rollback()
        raise

    db.session.commit()
    print("imported %s users" % created_count)
