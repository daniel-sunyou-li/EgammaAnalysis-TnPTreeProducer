import FWCore.ParameterSet.Config as cms

def setPileUpConfiguration(process, options):
  if    "2016APV" in options["era"]: from SimGeneral.MixingModule.mix_2016_25ns_UltraLegacy_PoissonOOTPU_cfi import mix
  if    "2016" in options["era"]: from SimGeneral.MixingModule.mix_2016_25ns_UltraLegacy_PoissonOOTPU_cfi import mix
  elif  "2017" in options['era']: from SimGeneral.MixingModule.mix_2017_25ns_UltraLegacy_PoissonOOTPU_cfi import mix
  elif  "2018" in options['era']: from SimGeneral.MixingModule.mix_2018_25ns_UltraLegacy_PoissonOOTPU_cfi import mix

  #### DATA PU DISTRIBUTIONS
  data_pu_distribs = {
    "Jamboree_golden_JSON" : [5.12e+04,3.66e+05,5.04e+05,4.99e+05,7.5e+05,1.1e+06,2.53e+06,9.84e+06,4.4e+07,1.14e+08,1.94e+08,2.63e+08,2.96e+08,2.74e+08,2.06e+08,1.26e+08,6.38e+07,2.73e+07,1.1e+07,5.2e+06,3.12e+06,1.87e+06,9.35e+05,3.64e+05,1.1e+05,2.64e+04,5.76e+03,1.53e+03,594,278,131,59.8,26,10.8,4.29,1.62,0.587,0.203,0.0669,0.0211,0.00633,0.00182,0.000498,0.00013,3.26e-05,7.77e-06,1.77e-06,3.85e-07,7.99e-08,1.58e-08,3e-09,5.43e-10],
    "ICHEP2016_JSON_4.0fb_xSec71.3mb" : [1.78e+03,2.69e+04,1.78e+05,4.71e+05,7.61e+05,1.02e+06,1.48e+06,7.35e+06,2.3e+07,3.75e+07,6.01e+07,9.32e+07,1.41e+08,2.09e+08,2.88e+08,3.53e+08,3.93e+08,4.09e+08,4e+08,3.69e+08,3.23e+08,2.69e+08,2.12e+08,1.57e+08,1.09e+08,6.96e+07,4.09e+07,2.19e+07,1.07e+07,4.8e+06,1.99e+06,7.76e+05,2.9e+05,1.07e+05,4.22e+04,1.95e+04,1.16e+04,8.73e+03,7.5e+03,6.85e+03,6.44e+03,6.16e+03,5.96e+03,5.81e+03,5.67e+03,5.53e+03,5.38e+03,5.21e+03,5.01e+03,4.78e+03],
    "ICHEP2016_JSON_5.7fb_xSec69.0mb" : [2.34e+03,7.7e+04,3.71e+05,7.77e+05,1.17e+06,1.64e+06,2.75e+06,1.34e+07,3.91e+07,8e+07,1.38e+08,1.94e+08,2.57e+08,3.41e+08,4.32e+08,5.08e+08,5.53e+08,5.63e+08,5.42e+08,4.98e+08,4.35e+08,3.6e+08,2.79e+08,2.01e+08,1.33e+08,8.23e+07,4.75e+07,2.58e+07,1.33e+07,6.59e+06,3.16e+06,1.47e+06,6.65e+05,2.91e+05,1.24e+05,5.3e+04,2.4e+04,1.28e+04,8.59e+03,7.04e+03,6.42e+03,6.13e+03,5.95e+03,5.79e+03,5.64e+03,5.47e+03,5.27e+03,5.04e+03,4.79e+03,4.51e+03],
    "ICHEP2016_JSON_12.9fb_xSec63.0mb": [5.05e+03,2.41e+05,7.83e+05,1.74e+06,2.37e+06,3.41e+06,6.12e+06,2.43e+07,6.78e+07,1.45e+08,2.57e+08,4.06e+08,5.63e+08,7.06e+08,8.41e+08,9.54e+08,1.03e+09,1.06e+09,1.06e+09,1.02e+09,9.47e+08,8.51e+08,7.41e+08,6.19e+08,4.93e+08,3.72e+08,2.67e+08,1.82e+08,1.18e+08,7.18e+07,4.13e+07,2.24e+07,1.15e+07,5.57e+06,2.56e+06,1.12e+06,4.7e+05,1.92e+05,7.78e+04,3.3e+04,1.61e+04,9.87e+03,7.67e+03,6.92e+03,6.66e+03,6.56e+03,6.49e+03,6.4e+03,6.28e+03,6.12e+03],
    "MORIOND2017_JSON_36fb_xSec69.2mb": [2.39e+05,8.38e+05,2.31e+06,3.12e+06,4.48e+06,6e+06,7e+06,1.29e+07,3.53e+07,7.87e+07,1.77e+08,3.6e+08,6.03e+08,8.77e+08,1.17e+09,1.49e+09,1.76e+09,1.94e+09,2.05e+09,2.1e+09,2.13e+09,2.15e+09,2.13e+09,2.06e+09,1.96e+09,1.84e+09,1.7e+09,1.55e+09,1.4e+09,1.24e+09,1.09e+09,9.37e+08,7.92e+08,6.57e+08,5.34e+08,4.27e+08,3.35e+08,2.58e+08,1.94e+08,1.42e+08,1.01e+08,6.9e+07,4.55e+07,2.88e+07,1.75e+07,1.02e+07,5.64e+06,2.99e+06,1.51e+06,7.32e+05,3.4e+05,1.53e+05,6.74e+04,3.05e+04,1.52e+04,8.98e+03,6.5e+03,5.43e+03,4.89e+03,4.52e+03,4.21e+03,3.91e+03,3.61e+03,3.32e+03,3.03e+03,2.75e+03,2.47e+03,2.21e+03,1.97e+03,1.74e+03,1.52e+03,1.32e+03,1.14e+03,983,839],
    "2017_DATA_xSec69.2mb_2Nov": [5.55e+04,1.81e+05,3.55e+05,1.16e+06,1.69e+06,2.36e+06,3.16e+06,3.54e+06,4.19e+06,6.16e+06,1.17e+07,2.41e+07,4.82e+07,8.91e+07,1.49e+08,2.29e+08,3.32e+08,4.53e+08,5.71e+08,6.74e+08,7.6e+08,8.22e+08,8.59e+08,8.88e+08,9.22e+08,9.64e+08,1.01e+09,1.04e+09,1.06e+09,1.05e+09,1.02e+09,9.58e+08,8.83e+08,7.96e+08,7.03e+08,6.06e+08,5.11e+08,4.2e+08,3.37e+08,2.64e+08,2.02e+08,1.51e+08,1.11e+08,7.93e+07,5.56e+07,3.83e+07,2.59e+07,1.73e+07,1.14e+07,7.37e+06,4.73e+06,3e+06,1.88e+06,1.17e+06,7.18e+05,4.37e+05,2.62e+05,1.56e+05,9.2e+04,5.37e+04,3.11e+04,1.79e+04,1.02e+04],
    "2017_DATA_xSec69.2mb_94X_17Jan": [2.6e+05,1.08e+06,2.09e+06,3.69e+06,4.09e+06,5.85e+06,6.31e+06,6.75e+06,9.53e+06,2.3e+07,4.52e+07,8.5e+07,1.32e+08,1.89e+08,2.68e+08,3.78e+08,5.29e+08,7.04e+08,8.77e+08,1.04e+09,1.18e+09,1.29e+09,1.37e+09,1.44e+09,1.5e+09,1.55e+09,1.6e+09,1.63e+09,1.64e+09,1.61e+09,1.57e+09,1.51e+09,1.43e+09,1.34e+09,1.24e+09,1.14e+09,1.04e+09,9.46e+08,8.64e+08,7.96e+08,7.46e+08,7.16e+08,7.08e+08,7.2e+08,7.47e+08,7.78e+08,8.03e+08,8.1e+08,7.89e+08,7.38e+08,6.59e+08,5.61e+08,4.56e+08,3.55e+08,2.65e+08,1.92e+08,1.35e+08,9.3e+07,6.34e+07,4.32e+07,2.97e+07,2.07e+07,1.48e+07,1.08e+07,8.14e+06,6.27e+06,4.93e+06,3.92e+06,3.14e+06,2.52e+06,2.02e+06,1.61e+06,1.28e+06,1.01e+06,7.85e+05,6.06e+05,4.63e+05,3.5e+05,2.61e+05,1.93e+05,1.4e+05,1.01e+05,7.14e+04,4.99e+04,3.44e+04,2.34e+04,1.56e+04,1.03e+04,6.67e+03,4.26e+03,2.67e+03,1.65e+03,1e+03,598,351,202,115,63.9,35,18.8],
    "2018_DATA_xSec69.2mb": [2.91e+05,1.02e+06,3.12e+06,6.82e+06,1.2e+07,1.86e+07,2.75e+07,4e+07,5.65e+07,7.82e+07,1.09e+08,1.53e+08,2.12e+08,2.9e+08,3.89e+08,5.1e+08,6.54e+08,8.22e+08,1.01e+09,1.2e+09,1.39e+09,1.56e+09,1.71e+09,1.83e+09,1.93e+09,2e+09,2.06e+09,2.12e+09,2.17e+09,2.22e+09,2.27e+09,2.32e+09,2.35e+09,2.37e+09,2.38e+09,2.37e+09,2.33e+09,2.27e+09,2.18e+09,2.07e+09,1.92e+09,1.76e+09,1.58e+09,1.38e+09,1.19e+09,1e+09,8.27e+08,6.69e+08,5.3e+08,4.12e+08,3.15e+08,2.37e+08,1.76e+08,1.29e+08,9.41e+07,6.78e+07,4.85e+07,3.45e+07,2.44e+07,1.72e+07,1.2e+07,8.34e+06,5.75e+06,3.93e+06,2.66e+06,1.78e+06,1.18e+06,7.72e+05,5e+05,3.21e+05,2.03e+05,1.27e+05,7.91e+04,4.87e+04,2.97e+04,1.79e+04,1.07e+04,6.35e+03,3.73e+03,2.17e+03,1.25e+03,714,402,224,123,67.1,36,19,9.93,5.1,2.58,1.29,0.632,0.305,0.145,0.0679,0.0313,0.0142,0.0063,0.00276],
    "2016
  }

  if   '2016' in options['era']: data_pu_distribution = data_pu_distribs['MORIOND2017_JSON_36fb_xSec69.2mb']
  elif '2017' in options['era']: data_pu_distribution = data_pu_distribs['2017_DATA_xSec69.2mb_94X_17Jan']
  elif '2018' in options['era']: data_pu_distribution = data_pu_distribs['2018_DATA_xSec69.2mb']

  process.pileupReweightingProducer = cms.EDProducer("PileupWeightProducer",
                                  pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
                                  PileupMC      = cms.vdouble(mix.input.nbPileupEvents.probValue),
                                  PileupData    = cms.vdouble(data_pu_distribution),
                                  )
  if options['useAOD']: process.pileupReweightingProducer.pileupInfoTag = "addPileupInfo"

  process.mc_sequence = cms.Sequence()
  if options['isMC'] : process.mc_sequence = cms.Sequence( process.pileupReweightingProducer )
