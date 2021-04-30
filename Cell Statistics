# Rotina que usa a ferramenta CellStatistics do ArcGIS

# Importa todos os módulos do arcpy
import arcpy

# Verifica a disponibilidade da extensão Spatial Analyst do ArcGIS
arcpy.CheckOutExtension("Spatial")

# Define o espaço de trabalho (Workspace) que armazena as imagens
arcpy.env.workspace = r'C:\*'

# Seleciona as imagens para aplicar a ferramenta CellStatistics
rasters = arcpy.ListRasters("*.tif")

# Operadores estatísticos do CellStatistics:
# MEAN — Calculates the mean (average) of the inputs.
# MAJORITY — Determines the majority (value that occurs most often) of the inputs.
# MAXIMUM — Determines the maximum (largest value) of the inputs.
# MEDIAN — Calculates the median of the inputs.
# MINIMUM — Determines the minimum (smallest value) of the inputs.
# MINORITY — Determines the minority (value that occurs least often) of the inputs.
# RANGE — Calculates the range (difference between largest and smallest value) of the inputs.
# STD — Calculates the standard deviation of the inputs.
# SUM — Calculates the sum (total of all values) of the inputs.
# VARIETY — Calculates the variety (number of unique values) of the inputs.

# Roda a ferramenta CellStatistics
calc = arcpy.sa.CellStatistics(rasters, statistics_type = '*')

# Salva as imagens de saída
calc.save(r'C:\*.tif')

