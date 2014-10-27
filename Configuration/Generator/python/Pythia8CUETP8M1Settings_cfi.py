import FWCore.ParameterSet.Config as cms

pythia8CUETP8M1SettingsBlock = cms.PSet(
    pythia8CUETP8M1Settings = cms.vstring(
        'Tune:pp 14',
        'Tune:ee 7',
        'MultipleInteractions:pT0Ref=2.4024',
        'MultipleInteractions:ecmPow=0.25208',
        'MultipleInteractions:expPow=1.6',
    )
)
