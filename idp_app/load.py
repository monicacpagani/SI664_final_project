# import csv
# from unesco.models import Site, Category, States, Region, Iso
#
# #fhand = open('unesco/whc-sites-2018-small.csv')
# #reader = csv.reader(fhand)
#
# Site.objects.all().delete()
# Category.objects.all().delete()
# States.objects.all().delete()
# Region.objects.all().delete()
# Iso.objects.all().delete()
#
#
#
# with open('unesco/whc-sites-2018-small.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     next(csvreader)
#     for row in csvreader:
#         #print(row)
#
#         try:
#             c = Category.objects.get(name=row[7])
#         except:
#             print("Inserting category",row[7])
#             c = Category(name=row[7])
#             c.save()
#
#         try:
#             s = States.objects.get(name=row[8])
#         except:
#             print("Inserting state",row[8])
#             s = States(name=row[8])
#             s.save()
#
#         try:
#             r = Region.objects.get(name=row[9])
#         except:
#             print("Inserting region",row[9])
#             r = Region(name=row[9])
#             r.save()
#
#         try:
#             i = Iso.objects.get(name=row[10])
#         except:
#             print("Inserting iso",row[10])
#             i = Iso(name=row[10])
#             i.save()
#
#         #Year
#         try:
#             y = int(row[3])
#         except:
#             y = None
#
#         #long
#         try:
#             x = float(row[4])
#         except:
#             x = None
#
#         #lat
#         try:
#             z = float(row[5])
#         except:
#             z = None
#
#         #area
#         try:
#             v = float(row[6])
#         except:
#             v = None
#
#
#         site = Site(name=row[0], description=row[1], year=y, justification=row[2], longitude=x, latitude=z, area_hectares=v, category=c, state=s, region=r, iso=i)
#         site.save()
