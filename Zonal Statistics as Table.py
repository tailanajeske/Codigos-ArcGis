# Name: Zonal Statistics as Table.py
# Description: Extracts the statistics of several rasters within an areas defined by a shpefile
# Requirements: ArcGIS Spatial Analyst Extension
# Status: 100% working

# Import system modules
import arcpy, os
from arcpy import env
from arcpy.sa import *

# Check the ArcGIS extension
arcpy.CheckOutExtension("Spatial")

# Overwrite the output data
arcpy.env.overwriteOutput = True

# Define the file directory (workspace) and destinations
env.workspace = "C:/*"
destination_path = 'C:/*'

#  Define the mask used to extract the cells
shapefile = "C:*.shp"
arcpy.MakeFeatureLayer_management(shapefile,"layer")
layer = arcpy.mapping.Layer("layer")

# Execute Zonal Statistics as Table in batch mode
# Na operação ZonalStatisticsAsTable: "Local" corresponde ao campo (field) da tabela de atributos (i.e.: classe de uso da terra, nome dos polígonos) que será usado para calcular as estatísticas
# Na operação ZonalStatisticsAsTable: "DATA" considera apenas valores válidos, excluindo valores NODATA das estatísticas
# Na operação ZonalStatisticsAsTable: "ALL" computa todas as estatisticas disponíveis na ferramenta (média, desvio, amplitude, etc.)
print "Calculating zonal statistics as table"

rasterlist = arcpy.ListDatasets("**.tif", "Raster")
for raster in rasterlist:
    destination_file = os.path.join(destination_path, raster)
    outZStat = ZonalStatisticsAsTable(layer, "Local", raster, destination_file,"DATA","ALL")

print 'Finished!'

# Merge dbf tables as a single file
print "Merging all dbf tables into a single file"
arcpy.env.workspace = 'C:*'
listTable = arcpy.ListTables()
arcpy.Merge_management(listTable, 'C:*.dbf')

print 'Finished!'
