# Generated by Django 2.2.1 on 2019-06-30 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import salesforce.backend.operations
import salesforce.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('home', '0026_auto_20190625_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mailing_country_code',
            field=salesforce.fields.CharField(blank=True, choices=[('AC', 'Acre'), ('AG', 'Agrigento'), ('AG', 'Aguascalientes'), ('AL', 'Alabama'), ('AL', 'Alagoas'), ('AK', 'Alaska'), ('AB', 'Alberta'), ('AL', 'Alessandria'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('AN', 'Ancona'), ('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('34', 'Anhui'), ('AO', 'Aosta'), ('AR', 'Arezzo'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AR', 'Arunachal Pradesh'), ('AP', 'Ascoli Piceno'), ('AS', 'Assam'), ('AT', 'Asti'), ('ACT', 'Australian Capital Territory'), ('AV', 'Avellino'), ('BA', 'Bahia'), ('BC', 'Baja California'), ('BS', 'Baja California Sur'), ('BA', 'Bari'), ('BT', 'Barletta-Andria-Trani'), ('11', 'Beijing'), ('BL', 'Belluno'), ('BN', 'Benevento'), ('BG', 'Bergamo'), ('BI', 'Biella'), ('BR', 'Bihar'), ('BO', 'Bologna'), ('BZ', 'Bolzano'), ('BS', 'Brescia'), ('BR', 'Brindisi'), ('BC', 'British Columbia'), ('CA', 'Cagliari'), ('CA', 'California'), ('CL', 'Caltanissetta'), ('CM', 'Campeche'), ('CB', 'Campobasso'), ('CI', 'Carbonia-Iglesias'), ('CW', 'Carlow'), ('CE', 'Caserta'), ('CT', 'Catania'), ('CZ', 'Catanzaro'), ('CN', 'Cavan'), ('CE', 'Ceará'), ('CH', 'Chandigarh'), ('CT', 'Chhattisgarh'), ('CS', 'Chiapas'), ('CH', 'Chieti'), ('CH', 'Chihuahua'), ('71', 'Chinese Taipei'), ('50', 'Chongqing'), ('CE', 'Clare'), ('CO', 'Coahuila'), ('CL', 'Colima'), ('CO', 'Colorado'), ('CO', 'Como'), ('CT', 'Connecticut'), ('CO', 'Cork'), ('CS', 'Cosenza'), ('CR', 'Cremona'), ('KR', 'Crotone'), ('CN', 'Cuneo'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DE', 'Delaware'), ('DL', 'Delhi'), ('DC', 'District of Columbia'), ('DF', 'Distrito Federal'), ('DL', 'Donegal'), ('D', 'Dublin'), ('DG', 'Durango'), ('EN', 'Enna'), ('ES', 'Espírito Santo'), ('DF', 'Federal District'), ('FM', 'Fermo'), ('FE', 'Ferrara'), ('FI', 'Florence'), ('FL', 'Florida'), ('FG', 'Foggia'), ('FC', 'Forlì-Cesena'), ('FR', 'Frosinone'), ('35', 'Fujian'), ('G', 'Galway'), ('62', 'Gansu'), ('GE', 'Genoa'), ('GA', 'Georgia'), ('GA', 'Goa'), ('GO', 'Goiás'), ('GO', 'Gorizia'), ('GR', 'Grosseto'), ('GT', 'Guanajuato'), ('44', 'Guangdong'), ('45', 'Guangxi'), ('GR', 'Guerrero'), ('52', 'Guizhou'), ('GJ', 'Gujarat'), ('46', 'Hainan'), ('HR', 'Haryana'), ('HI', 'Hawaii'), ('13', 'Hebei'), ('23', 'Heilongjiang'), ('41', 'Henan'), ('HG', 'Hidalgo'), ('HP', 'Himachal Pradesh'), ('91', 'Hong Kong'), ('42', 'Hubei'), ('43', 'Hunan'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IM', 'Imperia'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('IS', 'Isernia'), ('JA', 'Jalisco'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('32', 'Jiangsu'), ('36', 'Jiangxi'), ('22', 'Jilin'), ('KS', 'Kansas'), ('KA', 'Karnataka'), ('KY', 'Kentucky'), ('KL', 'Kerala'), ('KY', 'Kerry'), ('KE', 'Kildare'), ('KK', 'Kilkenny'), ('AQ', "L'Aquila"), ('LD', 'Lakshadweep'), ('LS', 'Laois'), ('SP', 'La Spezia'), ('LT', 'Latina'), ('LE', 'Lecce'), ('LC', 'Lecco'), ('LM', 'Leitrim'), ('21', 'Liaoning'), ('LK', 'Limerick'), ('LI', 'Livorno'), ('LO', 'Lodi'), ('LD', 'Longford'), ('LA', 'Louisiana'), ('LH', 'Louth'), ('LU', 'Lucca'), ('92', 'Macao'), ('MC', 'Macerata'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('ME', 'Maine'), ('MN', 'Manipur'), ('MB', 'Manitoba'), ('MN', 'Mantua'), ('MA', 'Maranhão'), ('MD', 'Maryland'), ('MS', 'Massa and Carrara'), ('MA', 'Massachusetts'), ('MT', 'Matera'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MO', 'Mayo'), ('MH', 'Meath'), ('VS', 'Medio Campidano'), ('ML', 'Meghalaya'), ('ME', 'Messina'), ('ME', 'Mexico State'), ('MI', 'Michigan'), ('MI', 'Michoacán'), ('MI', 'Milan'), ('MG', 'Minas Gerais'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MZ', 'Mizoram'), ('MO', 'Modena'), ('MN', 'Monaghan'), ('MT', 'Montana'), ('MB', 'Monza and Brianza'), ('MO', 'Morelos'), ('NL', 'Nagaland'), ('NA', 'Naples'), ('NA', 'Nayarit'), ('NE', 'Nebraska'), ('15', 'Nei Mongol'), ('NV', 'Nevada'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NSW', 'New South Wales'), ('NY', 'New York'), ('64', 'Ningxia'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NT', 'Northern Territory'), ('NT', 'Northwest Territories'), ('NO', 'Novara'), ('NS', 'Nova Scotia'), ('NL', 'Nuevo León'), ('NU', 'Nunavut'), ('NU', 'Nuoro'), ('OA', 'Oaxaca'), ('OR', 'Odisha'), ('OY', 'Offaly'), ('OG', 'Ogliastra'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OT', 'Olbia-Tempio'), ('ON', 'Ontario'), ('OR', 'Oregon'), ('OR', 'Oristano'), ('PD', 'Padua'), ('PA', 'Palermo'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PR', 'Parma'), ('PV', 'Pavia'), ('PA', 'Pennsylvania'), ('PE', 'Pernambuco'), ('PG', 'Perugia'), ('PU', 'Pesaro and Urbino'), ('PE', 'Pescara'), ('PC', 'Piacenza'), ('PI', 'Piauí'), ('PI', 'Pisa'), ('PT', 'Pistoia'), ('PN', 'Pordenone'), ('PZ', 'Potenza'), ('PO', 'Prato'), ('PE', 'Prince Edward Island'), ('PY', 'Puducherry'), ('PB', 'Puebla'), ('PB', 'Punjab'), ('63', 'Qinghai'), ('QC', 'Quebec'), ('QLD', 'Queensland'), ('QE', 'Querétaro'), ('QR', 'Quintana Roo'), ('RG', 'Ragusa'), ('RJ', 'Rajasthan'), ('RA', 'Ravenna'), ('RC', 'Reggio Calabria'), ('RE', 'Reggio Emilia'), ('RI', 'Rhode Island'), ('RI', 'Rieti'), ('RN', 'Rimini'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RM', 'Rome'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RN', 'Roscommon'), ('RO', 'Rovigo'), ('SA', 'Salerno'), ('SL', 'San Luis Potosí'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SK', 'Saskatchewan'), ('SS', 'Sassari'), ('SV', 'Savona'), ('SE', 'Sergipe'), ('61', 'Shaanxi'), ('37', 'Shandong'), ('31', 'Shanghai'), ('14', 'Shanxi'), ('51', 'Sichuan'), ('SI', 'Siena'), ('SK', 'Sikkim'), ('SI', 'Sinaloa'), ('SO', 'Sligo'), ('SO', 'Sondrio'), ('SO', 'Sonora'), ('SA', 'South Australia'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('SR', 'Syracuse'), ('TB', 'Tabasco'), ('TM', 'Tamaulipas'), ('TN', 'Tamil Nadu'), ('TA', 'Taranto'), ('TAS', 'Tasmania'), ('TN', 'Tennessee'), ('TE', 'Teramo'), ('TR', 'Terni'), ('TX', 'Texas'), ('12', 'Tianjin'), ('TA', 'Tipperary'), ('TL', 'Tlaxcala'), ('TO', 'Tocantins'), ('TP', 'Trapani'), ('TN', 'Trento'), ('TV', 'Treviso'), ('TS', 'Trieste'), ('TR', 'Tripura'), ('TO', 'Turin'), ('UD', 'Udine'), ('UT', 'Utah'), ('UT', 'Uttarakhand'), ('UP', 'Uttar Pradesh'), ('VA', 'Varese'), ('VE', 'Venice'), ('VE', 'Veracruz'), ('VB', 'Verbano-Cusio-Ossola'), ('VC', 'Vercelli'), ('VT', 'Vermont'), ('VR', 'Verona'), ('VV', 'Vibo Valentia'), ('VI', 'Vicenza'), ('VIC', 'Victoria'), ('VA', 'Virginia'), ('VT', 'Viterbo'), ('WA', 'Washington'), ('WD', 'Waterford'), ('WB', 'West Bengal'), ('WA', 'Western Australia'), ('WH', 'Westmeath'), ('WV', 'West Virginia'), ('WX', 'Wexford'), ('WW', 'Wicklow'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('65', 'Xinjiang'), ('54', 'Xizang'), ('YU', 'Yucatán'), ('YT', 'Yukon Territories'), ('53', 'Yunnan'), ('ZA', 'Zacatecas'), ('33', 'Zhejiang')], default=salesforce.backend.operations.DefaultedOnCreate(), max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='race',
            field=salesforce.fields.CharField(blank=True, choices=[('American Indian/Alaskan Native', 'American Indian/Alaskan Native'), ('Asian', 'Asian'), ('Black/African American', 'Black/African American'), ('Native Hawaiian/Other Pacific Islander', 'Native Hawaiian/Other Pacific Islander'), ('White', 'White'), ('American Indian/Alaskan Native AND Black/African American', 'American Indian/Alaskan Native AND Black/African American'), ('American Indian/Alaskan Native AND White', 'American Indian/Alaskan Native AND White'), ('Asian AND White', 'Asian AND White'), ('Black/African American AND White', 'Black/African American AND White'), ('Other/Multiracial', 'Other/Multiracial'), ('Politely Decline', 'Politely Decline')], max_length=255, null=True, verbose_name='Which best describes your race?'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='which_best_describes_your_ethnicity',
            field=salesforce.fields.CharField(blank=True, choices=[('Hispanic/Latinx', 'Hispanic/Latinx'), ('Not Hispanic/Latinx', 'Not Hispanic/Latinx'), ('Politely Decline', 'Politely Decline')], db_column='Which_best_describes_your_ethnicity__c', max_length=255, null=True, verbose_name='Which best describes your ethnicity?'),
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, unique=True)),
                ('announcement', models.TextField(max_length=2500)),
                ('posted', models.DateTimeField(auto_now=True, db_index=True)),
                ('email_recipients', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('recipient_classrooms', models.ManyToManyField(related_name='classroom', to='home.Classroom')),
                ('recipient_groups', models.ManyToManyField(related_name='user_groups', to='auth.Group')),
            ],
        ),
    ]