
#RAndKff  = {}
RAndKff['DYmva0p8'] = {
                      'RFile'   : '../DNN/rootFile/plots_BG_DY_NOHR_2017_MVA080_1j.root' ,
                      'KffFile' : '../DNN/rootFile/plots_BG_DY_NOHR_2017_MVA080_1j.root' ,
                      'Regions' : { '1jee' : {
                                               'kNum' : '1j_ee_in/events/histo_DY' ,
                                               'kDen' : '1j_uu_in/events/histo_DY' ,
                                               'RNum' : '1j_ee_out/events/histo_DY' ,
                                               'RDen' : '1j_ee_in/events/histo_DY' ,
                                             } ,
                                    '1jmm' : {
                                               'kNum' : '1j_uu_in/events/histo_DY' ,
                                               'kDen' : '1j_ee_in/events/histo_DY' ,
                                               'RNum' : '1j_uu_out/events/histo_DY' ,
                                               'RDen' : '1j_uu_in/events/histo_DY' ,
                                             } ,
                                   } ,
                     }


#DYestim = {}

DYestim['hww2l2v_13TeV_2017_1jee'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'rsyst'   : 0.10 , 
                                 'ksyst'   : 0.01 , 
                                 'njet'    : '1j'    ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2017_DYin_1jee' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_2017_DYin_1jdf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenorm1j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2017_1jee_HAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2017_1jee_AccDen/events/histo_DY',
                                 'asyst'   : 0.01 , 
                                } 

DYestim['hww2l2v_13TeV_2017_1jmm'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'rsyst'   : 0.10 , 
                                 'ksyst'   : 0.01 , 
                                 'njet'    : '1j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2017_DYin_1jmm' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_2017_DYin_1jdf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnorm1j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2017_1jmm_HAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2017_1jmm_AccDen/events/histo_DY',
                                 'asyst'   : 0.10 , 
                                } 

DYestim['hww2l2v_13TeV_2017_WW_1jee'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'njet'    : '1j'    ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2017_DYin_1jee' ,
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_2017_DYin_1jdf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenorm1j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2017_WW_1jee_WWAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2017_1jee_AccDen/events/histo_DY',
                                 'asyst'   : 0.01 , 
                                   }

DYestim['hww2l2v_13TeV_2017_WW_1jmm'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'njet'    : '1j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2017_DYin_1jmm' ,
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_2017_DYin_1jdf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnorm1j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2017_WW_1jmm_WWAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2017_1jmm_AccDen/events/histo_DY',
                                 'asyst'   : 0.03 ,
                                   }
