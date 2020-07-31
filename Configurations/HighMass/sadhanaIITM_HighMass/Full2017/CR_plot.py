# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#

groupPlot['top']  = {  
                  'nameHR' : 'tW and t#bar{t}',
                  'isSignal' : 0,
                  'color': 800,   # kOrange
                  'samples'  : ['top']
              }

groupPlot['WW']  = {  
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': 852, # kAzure -8
                  'samples'  : ['WW', 'ggWW', 'WWewk', 'qqWWqq', 'WW2J']
              }

groupPlot['Fake']  = {
                  'nameHR' : 'Nonprompt',
                  'isSignal' : 0,
                  'color': 922,    # kGray +2
                  'samples'  : ['Fake_me', 'Fake_em', 'Fake_ee', 'Fake_mm']
}


groupPlot['DY']  = {  
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color': 418,    # kGreen+2
                  'samples'  : ['DY', 'DYemb']
              }

groupPlot['VV']  = {  
                  'nameHR' : 'Multiboson',
                  'isSignal' : 0,
                  'color': 617,   # kViolet +1
                  'samples'  : ['VZ', 'WZ', 'ZZ', 'Vg', 'VgS_L', 'VgS_H', 'VVV']
              }

#groupPlot['VVV']  = {  
#                  'nameHR' : 'VVV',
#                  'isSignal' : 0,
#                  'color': 857, # kAzure -3  
#                  'samples'  : ['VVV']
#              }
#
#groupPlot['VZ']  = {  
#                  'nameHR' : "VZ",
#                  'isSignal' : 0,
#                  'color'    : 617,   # kViolet + 1  
#                  'samples'  : ['VZ', 'WZ', 'ZZ']
#              }
#
#groupPlot['Vg']  = {  
#                  'nameHR' : "V#gamma",
#                  'isSignal' : 0,
#                  'color'    : 810,   # kOrange + 10
#                  'samples'  : ['Vg']
#              }
#
#groupPlot['VgS']  = {
#                  'nameHR' : "V#gamma*",
#                  'isSignal' : 0,
#                  'color'    : 409,   # kGreen - 9
#                  'samples'  : ['VgS_L', 'VgS_H']
#              }

groupPlot['SMHiggs']  = {  
                  'nameHR' : 'SM Higgs',
                  'isSignal' : 0,
                  'color': 632, # kRed 
		  #'samples'  : ['ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww','bbH_hww','ttH_hww','ZH_htt', 'WH_htt', 'qqH_htt', 'ggH_htt']
		  'samples'  : ['ZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww', 'ZH_htt', 'WH_htt', 'qqH_htt', 'ggH_htt']
              }

groupPlot['HM_200']  = {  
                  'nameHR' : '200 GeV',
                  'isSignal' : 2,
                  'color': 2, # kRed 
                  'samples'  : ['GGH_200'+model_name, 'QQH_200'+model_name]
              }
groupPlot['HM_800']  = {  
                  'nameHR' : '800 GeV (x10)',
                  'isSignal' : 2,
                  'color': 3, # kRed 
                  'samples'  : ['GGH_800'+model_name, 'QQH_800'+model_name]
              }
groupPlot['HM_2000']  = {  
                  'nameHR' : '2000 GeV (x200)',
                  'isSignal' : 2,
                  'color': 4, # kRed 
                  'samples'  : ['GGH_2000'+model_name, 'QQH_2000'+model_name]
              }





#plot = {}

# keys here must match keys in samples.py    
#                    
plot['DY']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
              }

if useEmbeddedDY:
  plot['DYemb']  = {  
                    'color': 418,    # kGreen+2
                    'isSignal' : 0,
                    'isData'   : 0, 
                    'scale'    : 1.0,
                }

if EMorEEorMM == 'em':
  plot['Fake_me']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

  plot['Fake_em']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

if EMorEEorMM == 'ee':
  plot['Fake_ee']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

if EMorEEorMM == 'mm':
  plot['Fake_mm']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

plot['top'] = {   
                  'nameHR' : 'tW and t#bar{t}',
                  'color': 400,   # kYellow
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
                  }

plot['WW']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0
                  }

plot['ggWW']  = {
                  'color': 850, # kAzure -10
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0
                  }

plot['WWewk']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['WW2J']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['qqWWqq']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['Vg']  = { 
                  'color': 859, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VgS_L'] = { 
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VgS_H'] = { 
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VZ']  = { 
                  'color': 858, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VVV']  = { 
                  'color': 857, # kAzure -3  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

# Htautau
plot['ZH_htt'] = {
                  'nameHR' : 'ZHtt',
                  'color': 632+3, # kRed+3 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['WH_htt'] = {
                  'nameHR' : 'WHtt',
                  'color': 632+2, # kRed+2 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['qqH_htt'] = {
                  'nameHR' : 'qqHtt',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['ggH_htt'] = {
                  'nameHR' : 'ggHtt',
                  'color': 632, # kRed 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

# HWW 

#plot['H_hww'] = {
#                  'nameHR' : 'Hww',
#                  'color': 632, # kRed 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

plot['ZH_hww'] = {
                  'nameHR' : 'ZH',
                  'color': 632+3, # kRed+3 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

#plot['ggZH_hww'] = {
#                  'nameHR' : 'ggZH',
#                  'color': 632+4, # kRed+4
#                  'isSignal' : 0,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

plot['WH_hww'] = {
                  'nameHR' : 'WH',
                  'color': 632+2, # kRed+2 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['qqH_hww'] = {
                  'nameHR' : 'qqH',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['ggH_hww'] = {
                  'nameHR' : 'ggH',
                  'color': 632, # kRed 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

#plot['bbH_hww'] = {
#                  'nameHR' : 'bbH',
#                  'color': 632+5, # kRed+5 
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }

#plot['ttH_hww'] = {
#                  'nameHR' : 'ttH',
#                  'color': 632+6, # kRed+6
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }


massplot = ['200','800','2000']

for m in massplot:
  if m == '200':
    multggh = 1.0 * HiggsXS.GetHiggsXS4Sample('YR4','13TeV','GluGluHToWWTo2L2Nu_M200')['xs']
    multqqh = 1.0 * HiggsXS.GetHiggsXS4Sample('YR4','13TeV','VBFHToWWTo2L2Nu_M200')['xs']
  elif m == '800':
    multggh = 10.0 * HiggsXS.GetHiggsXS4Sample('YR4','13TeV','GluGluHToWWTo2L2Nu_M800')['xs']
    multqqh = 10.0 * HiggsXS.GetHiggsXS4Sample('YR4','13TeV','VBFHToWWTo2L2Nu_M800')['xs']
  elif m == '2000':
    multggh = 200.0 * HiggsXS.GetHiggsXS4Sample('YR4','13TeV','GluGluHToWWTo2L2Nu_M2000')['xs']
    multqqh = 200.0 * HiggsXS.GetHiggsXS4Sample('YR4','13TeV','VBFHToWWTo2L2Nu_M2000')['xs']

  plot['GGH_'+m+model_name] = {
                  'nameHR' : 'GGH'+m,
                  'color': 632+5, # kRed+5 
                  'isSignal' : 2,
                  'isData'   : 0,
                  'scale'    : multggh    #
                  }
#  plot['GGHSBI_'+m+model_name] = {
#                  'nameHR' : 'GGHSBI'+m,
#                  'color': 632+5, # kRed+5 
#                  'isSignal' : 2,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }

  plot['QQH_'+m+model_name] = {
                  'nameHR' : 'QQH'+m,
                  'color': 632+5, # kRed+5 
                  'isSignal' : 2,
                  'isData'   : 0,
                  'scale'    : multqqh    #
                  }
#  plot['QQHSBI_'+m+model_name] = {
#                  'nameHR' : 'QQHSBI'+m,
#                  'color': 632+5, # kRed+5 
#                  'isSignal' : 2,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }


# data

plot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 0
              }




# additional options

legend['lumi'] = 'L = 41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




