
#RAndKff  = {}
RAndKff['DYmva0p90'] = {
                      'RFile'   : 'rootFile/plots_DYESTIM2016_DYMVA090_v6.root' ,
                      'KffFile' : 'rootFile/plots_DYESTIM2016_DYMVA080_v6.root' ,
                      'Regions' : { '0jee' : {
                                               'kNum' : '0j_ee_in/events/histo_DY' ,
                                               'kDen' : '0j_mm_in/events/histo_DY' ,
                                               'RNum' : '0j_ee_out' ,
                                               'RDen' : '0j_ee_in' ,
                                             } ,
                                    '0jmm' : {
                                               'kNum' : '0j_mm_in/events/histo_DY' ,
                                               'kDen' : '0j_ee_in/events/histo_DY' ,
                                               'RNum' : '0j_mm_out' ,
                                               'RDen' : '0j_mm_in' ,
                                             } ,
                                    '1jee' : {
                                               'kNum' : '1j_ee_in/events/histo_DY' ,
                                               'kDen' : '1j_mm_in/events/histo_DY' ,
                                               'RNum' : '1j_ee_out' ,
                                               'RDen' : '1j_ee_in' ,
                                             } ,
                                    '1jmm' : {
                                               'kNum' : '1j_mm_in/events/histo_DY' ,
                                               'kDen' : '1j_ee_in/events/histo_DY' ,
                                               'RNum' : '1j_mm_out' ,
                                               'RDen' : '1j_mm_in' ,
                                             } ,
                                    '2jee' : {
                                               'kNum' : '2j_ee_in/events/histo_DY' ,
                                               'kDen' : '2j_mm_in/events/histo_DY' ,
                                               'RNum' : '2j_ee_out' ,
                                               'RDen' : '2j_ee_in' ,
                                             } ,
                                    '2jmm' : {
                                               'kNum' : '2j_mm_in/events/histo_DY' ,
                                               'kDen' : '2j_ee_in/events/histo_DY' ,
                                               'RNum' : '2j_mm_out' ,
                                               'RDen' : '2j_mm_in' ,
                                             } ,

                                   } ,
                     }

#DYestim = {}
DYestim['hww2l2v_13TeV_0j_ee'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'rsyst'   : 0.04 ,
                                 'ksyst'   : 0.03 ,
                                 'njet'    : '0j' ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_0j_ee' ,
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_0j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenorm0j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_0j_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_0j_ee/events/histo_DY',
                                 'asyst'   : 0.01 ,
                                }

DYestim['hww2l2v_13TeV_0j_mm'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'rsyst'   : 0.08 , 
                                 'ksyst'   : 0.07 , 
                                 'njet'    : '0j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_0j_mm' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_0j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnorm0j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_0j_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_0j_mm/events/histo_DY',
                                 'asyst'   : 0.02 , 
                                } 

DYestim['hww2l2v_13TeV_1j_ee'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'rsyst'   : 0.01 , 
                                 'ksyst'   : 0.01 , 
                                 'njet'    : '1j'    ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_1j_ee' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_1j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenorm1j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_1j_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_1j_ee/events/histo_DY',
                                 'asyst'   : 0.05 , 
                                } 

DYestim['hww2l2v_13TeV_1j_mm'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'rsyst'   : 0.02 , 
                                 'ksyst'   : 0.01 , 
                                 'njet'    : '1j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_1j_mm' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_1j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnorm1j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_1j_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_1j_mm/events/histo_DY',
                                 'asyst'   : 0.01 , 
                                } 

DYestim['hww2l2v_13TeV_2j_ee'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'rsyst'   : 0.05 ,
                                 'ksyst'   : 0.01 ,
                                 'njet'    : '2j'    ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_ee' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenorm2j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_ee/events/histo_DY',
                                 'asyst'   : 0.04 ,
                                }

DYestim['hww2l2v_13TeV_2j_mm'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'rsyst'   : 0.01 ,
                                 'ksyst'   : 0.01 ,
                                 'njet'    : '2j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_mm' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnorm2j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_mm/events/histo_DY',
                                 'asyst'   : 0.02 ,
                                }

DYestim['hww2l2v_13TeV_WW_0j_ee'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'njet'    : '0j'    ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_0j_ee' ,
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_0j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenorm0j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_0j_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_0j_ee/events/histo_DY',
                                 'asyst'   : 0.01 ,
                                   }

DYestim['hww2l2v_13TeV_WW_0j_mm'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'njet'    : '0j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_0j_mm' ,
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_0j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnorm0j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_0j_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_0j_mm/events/histo_DY',
                                 'asyst'   : 0.03 ,
                                   }

DYestim['hww2l2v_13TeV_WW_1j_ee'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'njet'    : '1j'    ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_1j_ee' ,
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_1j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenorm1j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_1j_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_1j_ee/events/histo_DY',
                                 'asyst'   : 0.01 ,
                                   }

DYestim['hww2l2v_13TeV_WW_1j_mm'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'njet'    : '1j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_1j_mm' ,
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_1j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnorm1j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_1j_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_1j_mm/events/histo_DY',
                                 'asyst'   : 0.04 ,
                                   }

DYestim['hww2l2v_13TeV_WW_2j_ee'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'njet'    : '2j'    ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_ee' ,
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenorm2j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_ee/events/histo_DY',
                                 'asyst'   : 0.01 ,
                                   }

DYestim['hww2l2v_13TeV_WW_2j_mm'] = {
                                 'rinout'  : 'DYmva0p90' ,
                                 'njet'    : '2j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_mm' ,
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_df' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnorm2j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_mm/events/histo_DY',
                                 'asyst'   : 0.01 ,
                                   }

