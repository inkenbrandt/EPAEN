# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# TRS_Model.py
# Created on: 2014-06-24 09:59:34.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: TRS_Model <SGID10_CADASTRE_PLSSSections_GCDB> <SGID10_CADASTRE_PLSSQuarterQuarterSections_GCDB> <CHEM_SAMPLES_MAJOR_IONS_2GRO__4_> <input> 
# Description: 
# PLSS and CAD
# ---------------------------------------------------------------------------

# Set the necessary product code
# import arcinfo


# Import arcpy module
import arcpy

# Script arguments
SGID10_CADASTRE_PLSSSections_GCDB = arcpy.GetParameterAsText(0)
if SGID10_CADASTRE_PLSSSections_GCDB == '#' or not SGID10_CADASTRE_PLSSSections_GCDB:
    SGID10_CADASTRE_PLSSSections_GCDB = "Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB" # provide a default value if unspecified

SGID10_CADASTRE_PLSSQuarterQuarterSections_GCDB = arcpy.GetParameterAsText(1)
if SGID10_CADASTRE_PLSSQuarterQuarterSections_GCDB == '#' or not SGID10_CADASTRE_PLSSQuarterQuarterSections_GCDB:
    SGID10_CADASTRE_PLSSQuarterQuarterSections_GCDB = "Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB" # provide a default value if unspecified

CHEM_SAMPLES_MAJOR_IONS_2GRO__4_ = arcpy.GetParameterAsText(2)
if CHEM_SAMPLES_MAJOR_IONS_2GRO__4_ == '#' or not CHEM_SAMPLES_MAJOR_IONS_2GRO__4_:
    CHEM_SAMPLES_MAJOR_IONS_2GRO__4_ = "C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj2" # provide a default value if unspecified

input = arcpy.GetParameterAsText(3)
if input == '#' or not input:
    input = "C:\\PROJECTS\\MLSNF\\Data\\GIS\\Chemistry.gdb\\input" # provide a default value if unspecified

# Local variables:
spajon2 = SGID10_CADASTRE_PLSSQuarterQuarterSections_GCDB
CHEM_SAMPLES_MAJOR_IONS_2GRO2__2_ = spajon2
CHEM_SAMPLES_MAJOR_IONS_2GRO2__3_ = CHEM_SAMPLES_MAJOR_IONS_2GRO2__2_
CHEM_SAMPLES_MAJOR_IONS_2GRO2__5_ = CHEM_SAMPLES_MAJOR_IONS_2GRO2__3_
projj2 = CHEM_SAMPLES_MAJOR_IONS_2GRO2__5_
CHEM_SAMPLES_MAJOR_IONS_2GRO__2_ = projj2
CHEM_SAMPLES_MAJOR_IONS_2GRO__5_ = CHEM_SAMPLES_MAJOR_IONS_2GRO__2_
CHEM_SAMPLES_MAJOR_IONS_2GRO__6_ = CHEM_SAMPLES_MAJOR_IONS_2GRO__5_
PLSSQuarterQuarterSections_G2 = SGID10_CADASTRE_PLSSQuarterQuarterSections_GCDB
spajon1 = SGID10_CADASTRE_PLSSSections_GCDB
projj = input

# Process: Project
arcpy.Project_management(input, projj, "PROJCS['NAD_1983_UTM_Zone_12N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-111.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", "", "PROJCS['NAD_1983_UTM_Zone_12N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-111.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]")

# Process: Spatial Join
arcpy.SpatialJoin_analysis(projj, SGID10_CADASTRE_PLSSSections_GCDB, spajon1, "JOIN_ONE_TO_ONE", "KEEP_ALL", "FRSTDIVID \"First Division Identifer\" true true false 22 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,FRSTDIVID,-1,-1;TOWNSHIP \"TOWNSHIP\" true true false 5 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,TOWNSHIP,-1,-1;RANGE \"RANGE\" true true false 5 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,RANGE,-1,-1;SECTION \"SECTION\" true true false 2 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,SECTION,-1,-1;BASEMERIDIAN \"BASEMERIDIAN\" true true false 2 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,BASEMERIDIAN,-1,-1;LABEL \"LABEL\" true true false 20 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,LABEL,-1,-1;FRSTDIVNO \"First Division Number\" true true false 3 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,FRSTDIVNO,-1,-1;FRSTDIVDUP \"First Division Duplicate\" true true false 1 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,FRSTDIVDUP,-1,-1;FRSTDIVTYP \"First Division Type Code\" true true false 2 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,FRSTDIVTYP,-1,-1;FRSTDIVTXT \"First Division Type Description\" true true false 50 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,FRSTDIVTXT,-1,-1;PLSSID \"PLSS Identifier\" true true false 16 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,PLSSID,-1,-1;FRSTDIVLAB \"First Division Label\" true true false 15 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,FRSTDIVLAB,-1,-1;SURVTYP \"SURVTYP\" true true false 2 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,SURVTYP,-1,-1;SURVTYPTXT \"SURVTYPTXT\" true true false 50 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,SURVTYPTXT,-1,-1;TNUM \"TNUM\" true true false 8 Double 8 38 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,TNUM,-1,-1;RNUM \"RNUM\" true true false 8 Double 8 38 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,RNUM,-1,-1;SNUM \"SNUM\" true true false 4 Long 0 10 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,SNUM,-1,-1;QNUM \"QNUM\" true true false 4 Long 0 10 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,QNUM,-1,-1;Shape_area \"Shape_area\" false false true 0 Double 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,Shape.area,-1,-1;Shape_len \"Shape_len\" false false true 0 Double 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSSections_GCDB,Shape.len,-1,-1;SampleId \"Sample Id\" true true false 100 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,SampleId,-1,-1;StationId \"Station Id\" true true false 50 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,StationId,-1,-1;Sample_Date \"Sample_Date\" true true false 8 Date 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Sample_Date,-1,-1;As_diss \"As_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,As_diss,-1,-1;Ca \"Ca\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Ca,-1,-1;Cl \"Cl\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Cl,-1,-1;CO2 \"CO2\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,CO2,-1,-1;CO3 \"CO3\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,CO3,-1,-1;Cond \"Cond\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Cond,-1,-1;Cu_diss \"Cu_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Cu_diss,-1,-1;DO \"DO\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,DO,-1,-1;Fe_diss \"Fe_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Fe_diss,-1,-1;HCO3 \"HCO3\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,HCO3,-1,-1;K \"K\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,K,-1,-1;Meas_Alk \"Meas_Alk\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Meas_Alk,-1,-1;Meas_Hardness \"Meas_Hardness\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Meas_Hardness,-1,-1;Mg \"Mg\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Mg,-1,-1;Na \"Na\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Na,-1,-1;NO2 \"NO2\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,NO2,-1,-1;NO3 \"NO3\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,NO3,-1,-1;Pb_diss \"Pb_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Pb_diss,-1,-1;pH_lab \"pH_lab\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,pH_lab,-1,-1;Se_diss \"Se_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Se_diss,-1,-1;Si \"Si\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Si,-1,-1;SO4 \"SO4\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,SO4,-1,-1;TDS \"TDS\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,TDS,-1,-1;Temp \"Temp\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Temp,-1,-1;Zn_diss \"Zn_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Zn_diss,-1,-1;BAL \"BAL\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,BAL,-1,-1;Elev \"Elev\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Elev,-1,-1;Coord_Lat \"Coord_Lat\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Coord_Lat,-1,-1;Coord_Long \"Coord_Long\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Coord_Long,-1,-1;Geology \"Geology\" true true false 50 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Geology,-1,-1;Type \"Type\" true true false 50 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,Type,-1,-1;LnK \"LnK\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,LnK,-1,-1;LnMg \"LogMg\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,LnMg,-1,-1;LnNa \"LogNa\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,LnNa,-1,-1;LnHCO3 \"LogHCO3\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,LnHCO3,-1,-1;LnCl \"LogCl\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,LnCl,-1,-1;LnSO4 \"LnSO4\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,LnSO4,-1,-1;LnCa \"LnCa\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,LnCa,-1,-1;LnCon \"LnCon\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,LnCon,-1,-1;unid \"unid\" true true false 2 Short 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\projj,unid,-1,-1", "INTERSECT", "", "")

# Process: Spatial Join (2)
arcpy.SpatialJoin_analysis(spajon1, SGID10_CADASTRE_PLSSQuarterQuarterSections_GCDB, spajon2, "JOIN_ONE_TO_ONE", "KEEP_ALL", "SECDIVID \"Second Division Identifier\" true true false 25 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,SECDIVID,-1,-1;FRSTDIVID_1 \"First Division Identifier\" true true false 25 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,FRSTDIVID,-1,-1;SECDIVNO \"Second Division Number or Designator\" true true false 50 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,SECDIVNO,-1,-1;SECDIVSUF \"Second Division Suffix\" true true false 10 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,SECDIVSUF,-1,-1;SECDIVTYP \"Second Division Type Code\" true true false 1 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,SECDIVTYP,-1,-1;SECDIVTXT \"Second Division Type Text\" true false false 50 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,SECDIVTXT,-1,-1;ACRES \"Area in Acres\" true true false 8 Double 8 38 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,ACRES,-1,-1;PLSSID_1 \"PLSS Township Identifier\" true true false 16 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,PLSSID,-1,-1;SECDIVLAB \"Second Division Label\" true true false 50 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,SECDIVLAB,-1,-1;SURVTYP_1 \"Survey Type Code\" true true false 2 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,SURVTYP,-1,-1;SURVTYPTXT_1 \"Survey Type Text\" true true false 50 Text 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,SURVTYPTXT,-1,-1;SHAPE_area_1 \"SHAPE_area_1\" false false true 0 Double 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,SHAPE.area,-1,-1;SHAPE_len_1 \"SHAPE_len_1\" false false true 0 Double 0 0 ,First,#,Database Connections\\AGRC_SGID.sde\\SGID10.CADASTRE.PLSSQuarterQuarterSections_GCDB,SHAPE.len,-1,-1;Join_Count \"Join_Count\" true true false 0 Long 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Join_Count,-1,-1;TARGET_FID \"TARGET_FID\" true true false 0 Long 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,TARGET_FID,-1,-1;FRSTDIVID \"First Division Identifer\" true true false 22 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,FRSTDIVID,-1,-1;TOWNSHIP \"TOWNSHIP\" true true false 5 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,TOWNSHIP,-1,-1;RANGE \"RANGE\" true true false 5 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,RANGE,-1,-1;SECTION \"SECTION\" true true false 2 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,SECTION,-1,-1;BASEMERIDIAN \"BASEMERIDIAN\" true true false 2 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,BASEMERIDIAN,-1,-1;LABEL \"LABEL\" true true false 20 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,LABEL,-1,-1;FRSTDIVNO \"First Division Number\" true true false 3 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,FRSTDIVNO,-1,-1;FRSTDIVDUP \"First Division Duplicate\" true true false 1 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,FRSTDIVDUP,-1,-1;FRSTDIVTYP \"First Division Type Code\" true true false 2 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,FRSTDIVTYP,-1,-1;FRSTDIVTXT \"First Division Type Description\" true true false 50 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,FRSTDIVTXT,-1,-1;PLSSID \"PLSS Identifier\" true true false 16 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,PLSSID,-1,-1;FRSTDIVLAB \"First Division Label\" true true false 15 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,FRSTDIVLAB,-1,-1;SURVTYP \"SURVTYP\" true true false 2 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,SURVTYP,-1,-1;SURVTYPTXT \"SURVTYPTXT\" true true false 50 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,SURVTYPTXT,-1,-1;TNUM \"TNUM\" true true false 8 Double 8 38 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,TNUM,-1,-1;RNUM \"RNUM\" true true false 8 Double 8 38 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,RNUM,-1,-1;SNUM \"SNUM\" true true false 4 Long 0 10 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,SNUM,-1,-1;QNUM \"QNUM\" true true false 4 Long 0 10 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,QNUM,-1,-1;Shape_area \"Shape_area\" false false true 0 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Shape_area,-1,-1;Shape_len \"Shape_len\" false false true 0 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Shape_len,-1,-1;SampleId \"Sample Id\" true true false 100 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,SampleId,-1,-1;StationId \"Station Id\" true true false 50 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,StationId,-1,-1;Sample_Date \"Sample_Date\" true true false 8 Date 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Sample_Date,-1,-1;As_diss \"As_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,As_diss,-1,-1;Ca \"Ca\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Ca,-1,-1;Cl \"Cl\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Cl,-1,-1;CO2 \"CO2\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,CO2,-1,-1;CO3 \"CO3\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,CO3,-1,-1;Cond \"Cond\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Cond,-1,-1;Cu_diss \"Cu_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Cu_diss,-1,-1;DO \"DO\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,DO,-1,-1;Fe_diss \"Fe_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Fe_diss,-1,-1;HCO3 \"HCO3\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,HCO3,-1,-1;K \"K\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,K,-1,-1;Meas_Alk \"Meas_Alk\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Meas_Alk,-1,-1;Meas_Hardness \"Meas_Hardness\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Meas_Hardness,-1,-1;Mg \"Mg\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Mg,-1,-1;Na \"Na\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Na,-1,-1;NO2 \"NO2\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,NO2,-1,-1;NO3 \"NO3\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,NO3,-1,-1;Pb_diss \"Pb_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Pb_diss,-1,-1;pH_lab \"pH_lab\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,pH_lab,-1,-1;Se_diss \"Se_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Se_diss,-1,-1;Si \"Si\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Si,-1,-1;SO4 \"SO4\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,SO4,-1,-1;TDS \"TDS\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,TDS,-1,-1;Temp \"Temp\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Temp,-1,-1;Zn_diss \"Zn_diss\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Zn_diss,-1,-1;BAL \"BAL\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,BAL,-1,-1;Elev \"Elev\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Elev,-1,-1;Coord_Lat \"Coord_Lat\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Coord_Lat,-1,-1;Coord_Long \"Coord_Long\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Coord_Long,-1,-1;Geology \"Geology\" true true false 50 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Geology,-1,-1;Type \"Type\" true true false 50 Text 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,Type,-1,-1;LnK \"LnK\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,LnK,-1,-1;LnMg \"LogMg\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,LnMg,-1,-1;LnNa \"LogNa\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,LnNa,-1,-1;LnHCO3 \"LogHCO3\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,LnHCO3,-1,-1;LnCl \"LogCl\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,LnCl,-1,-1;LnSO4 \"LnSO4\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,LnSO4,-1,-1;LnCa \"LnCa\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,LnCa,-1,-1;LnCon \"LnCon\" true true false 8 Double 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,LnCon,-1,-1;unid \"unid\" true true false 2 Short 0 0 ,First,#,C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\spajon1,unid,-1,-1", "INTERSECT", "", "")

# Process: Feature To Point
arcpy.FeatureToPoint_management(SGID10_CADASTRE_PLSSQuarterQuarterSections_GCDB, PLSSQuarterQuarterSections_G2, "CENTROID")

# Process: Near
arcpy.Near_analysis(spajon2, "C:\\Users\\PAULINKENBRANDT\\Documents\\ArcGIS\\Default.gdb\\PLSSQuarterQuarterSections_G2", "", "NO_LOCATION", "ANGLE", "PLANAR")

# Process: Add Field
arcpy.AddField_management(CHEM_SAMPLES_MAJOR_IONS_2GRO2__2_, "PLSS", "TEXT", "", "", "20", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(CHEM_SAMPLES_MAJOR_IONS_2GRO2__3_, "PLSS", "quarterfill(!TNUM!,!RNUM!,!SNUM!,!QNUM!,!SECDIVNO!,!NEAR_ANGLE!)", "PYTHON_9.3", "def quarterfill(tow, ran, sec, quad, x, a):\\n    g=x[0:2]\\n    h=x[2:4]\\n    m = {'NE':'a','NW':'b','SW':'c','SE':'d'}\\n    n = {1:'A',2:'B',3:'C',4:'D'}\\n    qq = m.get(g) or ''\\n    q = m.get(h) or ''\\n    j = n.get(quad) or ''\\n    if a > 90:\\n        qqq='d'\\n    elif a <-90:\\n        qqq='a'\\n    elif a < 90 and a > 0:\\n        qqq = 'c'\\n    elif a < 0 and a > -90:\\n        qqq = 'b'\\n    else:\\n        qqq = ''\\n    return '('+ str(j)+'-'+ str(int(tow)).rjust(2) + '-' + str(int(ran)).rjust(2)+')'+ str(int(sec)).rjust(2) + q + qq + qqq")

# Process: Project (2)
arcpy.Project_management(CHEM_SAMPLES_MAJOR_IONS_2GRO2__5_, projj2, "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", "", "")

# Process: Add XY Coordinates
arcpy.AddXY_management(projj2)

# Process: Add Field (2)
arcpy.AddField_management(CHEM_SAMPLES_MAJOR_IONS_2GRO__2_, "USGSCAD", "TEXT", "", "", "20", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)
arcpy.CalculateField_management(CHEM_SAMPLES_MAJOR_IONS_2GRO__5_, "PLSS", "decdeg(!POINT_X!,!POINT_Y!)", "PYTHON_9.3", "def decdeg(x,y):\\n  degx = int(abs(x))\\n  degy = int(abs(y))\\n  tempx = 60* (abs(x) - degx)\\n  tempy = 60* (abs(y) - degy)\\n  minx = int(tempx)\\n  miny = int(tempy)\\n  secx = str(int(round(60*(tempx-minx),0))).zfill(2)\\n  secy = str(int(round(60*(tempy-miny),0))).zfill(2)\\n  return str(degy).zfill(2)+str(miny).zfill(2)+str(secy).zfill(2)+str(degx).zfill(2)+str(minx).zfill(2)+str(secx).zfill(2)")

# Process: Delete Field
arcpy.DeleteField_management(CHEM_SAMPLES_MAJOR_IONS_2GRO__6_, "Join_Count;TARGET_FID;SECDIVID;FRSTDIVID_1;SECDIVNO;SECDIVSUF;SECDIVTYP;SECDIVTXT;ACRES;PLSSID_1;SECDIVLAB;SURVTYP_1;SURVTYPTXT_1;Join_Count_1;TARGET_FID_1;FRSTDIVID;TOWNSHIP;RANGE;SECTION;BASEMERIDIAN;FRSTDIVNO;FRSTDIVDUP;FRSTDIVTYP;FRSTDIVTXT;PLSSID;FRSTDIVLAB;SURVTYP;SURVTYPTXT;TNUM;RNUM;SNUM;QNUM;NEAR_FID;NEAR_DIST;NEAR_ANGLE")

