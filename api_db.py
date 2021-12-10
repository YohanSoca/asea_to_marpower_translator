import numpy as np

api_data_base = np.array( [
    {
        'name': 'L1 current',
        'asea_cmd': ':MEASure:SP1:CURRent1',
        'desc': 'Shore Power A RMS Current Real number, 0 to 1000',
        'spc_register': '1005',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'L2 current',
        'asea_cmd': ':MEASure:SP1:CURRent2',
        'desc': 'Shore Power B RMS Current Real number, 0 to 1000',
        'spc_register': '1006',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'L3 current',
        'asea_cmd': ':MEASure:SP1:CURRent3',
        'desc': 'Shore Power C RMS Current Real number, 0 to 1000',
        'spc_register': '1007',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    }, 
    {
        'name': 'L1 KVA',
        'asea_cmd': ':MEASure:SP1:KVA1',
        'desc': 'Shore Power Phase A kVA Real number, 0 to 1000',
        'spc_register': '1013',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'L2 KVA',
        'asea_cmd': ':MEASure:SP1:KVA2',
        'desc': 'Shore Power Phase B kVA Real number, 0 to 1000',
        'spc_register': '1013',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    }, 
    {
        'name': 'L3 KVA',
        'asea_cmd': ':MEASure:SP1:KVA3',
        'desc': 'Shore Power Phase C kVA Real number, 0 to 1000',
        'spc_register': '1013',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'L1 KW',
        'asea_cmd': ':MEASure:SP1:POWer1',
        'desc': 'Shore Power Phase A kW Real number, 0 to 1000',
        'spc_register': '100B',
        'type': 'keep-alive', 
        'last-query': '',
        'value': ''
    },
    {
        'name': 'L2 KW',
        'asea_cmd': ':MEASure:SP1:POWer2',
        'desc': 'Shore Power Phase B kW Real number, 0 to 1000',
        'spc_register': '100B',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'L3 KW',
        'asea_cmd': ':MEASure:SP1:POWer3',
        'desc': 'Shore Power Phase C kW Real number, 0 to 1000',
        'spc_register': '100B',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'L1 power factor',
        'asea_cmd': ':MEASure:SP1:PF1',
        'desc': 'Shore Power Phase A Power Factor Real number, 0 to 1.00',
        'spc_register': '1010',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'L2 power factor',
        'asea_cmd': ':MEASure:SP1:PF2',
        'desc': 'Shore Power Phase B Power Factor Real number, 0 to 1.00',
        'spc_register': '1012',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'L3 power factor',
        'asea_cmd': ':MEASure:SP1:PF3',
        'desc': 'Shore Power Phase C Power Factor Real number, 0 to 1.00',
        'spc_register': '1013',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Asea all',
        'asea_cmd': ':MEASure:SP1:ALL',
        'desc': 'VLL1,VLL2,VLL3,CURR1, See above, expressed in CURR2,CURR3,FREQ 3.2 precision',
        'spc_register': '1014',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    }, 
    {
        'name': 'Converter frecuency',
        'asea_cmd': ':MEASure:CONVerter:FREQuency',
        'desc': 'Converter Output Frequency Real number, 0 to 100',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '1015',
        'value': ''
    },
    {
        'name': 'Converter L1 voltage',
        'asea_cmd': ':MEASure:CONVerter:VOLTage1',
        'desc': 'Converter Phase A Output Voltage Real number, 0 to 1000',
        'spc_register': '1016',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter L2 voltage',
        'asea_cmd': ':MEASure:CONVerter:VOLTage2',
        'desc': 'Converter Phase B Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    }, 
    {
        'name': 'Converter L3 voltage',
        'asea_cmd': ':MEASure:CONVerter:VOLTage13',
        'desc': 'Converter Phase C Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase A-B Output Voltage',
        'asea_cmd': ':MEASure:CONVerter:VLL1',
        'desc': 'Converter Phase A-B Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase B-C Output Voltage',
        'asea_cmd': ':MEASure:CONVerter:VLL2',
        'desc': 'Converter Phase B-C Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase C-A Output Voltage',
        'asea_cmd': ':MEASure:CONVerter:VLL3',
        'desc': 'Converter Phase C-A Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter A RMS Current',
        'asea_cmd': ':MEASure:CONVerter:CURRent1',
        'desc': 'Converter A RMS Current Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter B RMS Current',
        'asea_cmd': ':MEASure:CONVerter:CURRent2',
        'desc': 'Converter B RMS Current Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter C RMS Current',
        'asea_cmd': ':MEASure:CONVerter:CURRent3',
        'desc': 'Converter C RMS Current Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase A kVA',
        'asea_cmd': ':MEASure:CONVerter:KVA1',
        'desc': 'Converter Phase A kVA Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase B kVA',
        'asea_cmd': ':MEASure:CONVerter:KVA2',
        'desc': 'Converter Phase B kVA Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase C kVA',
        'asea_cmd': ':MEASure:CONVerter:KVA3',
        'desc': 'Converter Phase C kVA Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase A kW',
        'asea_cmd': ':MEASure:CONVerter:POWer1',
        'desc': 'Converter Phase A kW Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase B kW',
        'asea_cmd': ':MEASure:CONVerter:POWer2',
        'desc': 'Converter Phase B kW Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        
        'name': 'Converter Phase C kW',
        'asea_cmd': ':MEASure:CONVerter:POWer3',
        'desc': 'Converter Phase C kW Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase A Power Factor',
        'asea_cmd': ':MEASure:CONVerter:PF1',
        'desc': 'Converter Phase A Power Factor Real number, 0 to 1.00',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase B Power Factor',
        'asea_cmd': ':MEASure:CONVerter:PF2',
        'desc': 'Converter Phase B Power Factor Real number, 0 to 1.00',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Phase C Power Factor',
        'asea_cmd': ':MEASure:CONVerter:PF3',
        'desc': 'Converter Phase C Power Factor Real number, 0 to 1.00',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'VOLT1, VOLT2, VOLT3, CURR1, CURR2, CURR3, FREQ',
        'asea_cmd': ':MEASure:CONVerter:ALL',
        'desc': 'VOLT1, VOLT2, VOLT3, CURR1, See above, expressed in CURR2, CURR3, FREQ 3.2 precision',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Generator #1 Output Frequency',
        'asea_cmd': ':MEASure:GENerator1:FREQuency',
        'desc': 'Generator #1 Output Frequency Real number, 0 to 100',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Generator #1 Phase A Output Voltage',
        'asea_cmd': ':MEASure:GENerator1:VOLTage1',
        'desc': 'Generator #1 Phase A Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Generator #1 Phase B Output Voltage',
        'asea_cmd': ':MEASure:GENerator1:VOLTage2',
        'desc': 'Generator #1 Phase B Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Generator #1 Phase C Output Voltage',
        'asea_cmd': ':MEASure:GENerator1:VOLTage3',
        'desc': 'Generator #1 Phase C Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Generator #2 Output Frequency',
        'asea_cmd': ':MEASure:GENerator2:FREQuency',
        'desc': 'Generator #2 Output Frequency Real number, 0 to 100',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
     {
        'name': 'Generator #2 Phase A Output Voltage',
        'asea_cmd': ':MEASure:GENerator2:VOLTage1',
        'desc': 'Generator #2 Phase A Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Generator #2 Phase A Output Voltage',
        'asea_cmd': ':MEASure:GENerator2:VOLTage1',
        'desc': 'Generator #2 Phase A Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Generator #2 Phase A Output Voltage',
        'asea_cmd': ':MEASure:GENerator2:VOLTage2',
        'desc': 'Generator #2 Phase A Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Generator #2 Phase A Output Voltage',
        'asea_cmd': ':MEASure:GENerator2:VOLTage3',
        'desc': 'Generator #2 Phase A Output Voltage Real number, 0 to 1000',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': '(GEN1) VOLT1, VOLT2, VOLT3, FREQ (GEN2) VOLT1, VOLT2, VOLT3, FREQ',
        'asea_cmd': ':MEASure:GENerator:ALL',
        'desc': 'GEN1) VOLT1, VOLT2, VOLT3, See above, reduced to FREQ, (GEN2) VOLT1, VOLT2, 3.2 resolution VOLT3, FREQ',
        'spc_register': '',
        'type': 'keep-alive',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Shore Power ON',
        'asea_cmd': ':SHORe:ON',
        'desc': 'Shore Power ON Same as pressing the Shore Power ON key on the panel',
        'spc_register': '',
        'type': 'one-time',
        'last-query': '', 'value': ''
    },
    {
        'name': 'Shore Power OFF',
        'asea_cmd': ':SHORe:OFF',
        'desc': 'Shore Power OFF Same as pressing the Shore Power OFF key on the panel',
        'spc_register': '',
        'type': 'one-time',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Power ON',
        'asea_cmd': ':CONVerter:ON',
        'desc': 'Converter Power ON Same as pressing the Converter Power ON key on the panel',
        'spc_register': '',
        'type': 'one-time',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Converter Power OFF',
        'asea_cmd': ':CONVerter:OFF',
        'desc': 'Converter Power OFF Same as pressing the Converter Power OFF key on the panel',
        'spc_register': '',
        'type': 'one-time',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Transfer from Generator to Converter',
        'asea_cmd': ':TS:CONVerter:ON',
        'desc': 'Transfer from Generator to Converter',
        'spc_register': '',
        'type': 'one-time',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Transfer from Converter to Generator',
        'asea_cmd': ':TS:GENerator:ON',
        'desc': 'Transfer from Converter to Generator',
        'spc_register': '',
        'type': 'one-time',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Set Generator 1 as transfer master',
        'asea_cmd': ':TS:G1:MASTer',
        'desc': 'Set Generator 1 as transfer master Same as pressing the GENERATOR display key, then F1',
        'spc_register': '',
        'type': 'one-time',
        'last-query': '',
        'value': ''
    },
    {
        'name': 'Set Generator 2 as transfer master',
        'asea_cmd': ':TS:G2:MASTer',
        'desc': 'Set Generator 2 as transfer master Same as pressing the GENERATOR display key, then F2',
        'spc_register': '',
        'type': 'one-time',
        'last-query': '',
        'value': ''
    }
])

