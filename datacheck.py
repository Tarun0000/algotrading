from main import api
import datetime
import timeit
import logging
import pandas as pd
import json
import talib as t
import matplotlib.pyplot as plt
from datetime import timedelta

end = datetime.datetime.today()


def datacheck(eqname, data):
    open = data['into']
    high = data['inth']
    low = data['intl']
    close = data['intc']
    final_list = {eqname: []}

    integer = t.CDL3BLACKCROWS(open, high, low, close)
    temp = {'Three Black Crows': []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Three Black Crows'].append(data['time'][ind])
    if len(temp['Three Black Crows']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDL3INSIDE(open, high, low, close)
    temp = {"Three Inside Up/Down": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Three Inside Up/Down'].append(data['time'][ind])
    if len(temp['Three Inside Up/Down']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDL3LINESTRIKE(open, high, low, close)
    temp = {"Three-Line Strike": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Three-Line Strike'].append(data['time'][ind])
    if len(temp['Three-Line Strike']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDL3OUTSIDE(open, high, low, close)
    temp = {"Harami": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Harami'].append(data['time'][ind])
    if len(temp['Harami']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDL3STARSINSOUTH(open, high, low, close)
    temp = {"Three Stars In The South/Down": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Three Stars In The South/Down'].append(data['time'][ind])
    if len(temp['Three Stars In The South/Down']) > 0:
        final_list[eqname].append(temp)

    temp = {"Three Advancing White Soldiers": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Three Advancing White Soldiers'].append(data['time'][ind])
    if len(temp['Three Advancing White Soldiers']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLABANDONEDBABY(open, high, low, close, penetration=0)
    temp = {"Abandoned Baby": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Abandoned Baby'].append(data['time'][ind])
    if len(temp['Abandoned Baby']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLADVANCEBLOCK(open, high, low, close)
    temp = {"Advance Block": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Advance Block'].append(data['time'][ind])
    if len(temp['Advance Block']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLBELTHOLD(open, high, low, close)
    temp = {"Belt-hold": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Belt-hold'].append(data['time'][ind])
    if len(temp['Belt-hold']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLBREAKAWAY(open, high, low, close)
    temp = {"Breakaway": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Breakaway'].append(data['time'][ind])
    if len(temp['Breakaway']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLCLOSINGMARUBOZU(open, high, low, close)
    temp = {"Closing Marubozu": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Closing Marubozu'].append(data['time'][ind])
    if len(temp['Closing Marubozu']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLCONCEALBABYSWALL(open, high, low, close)
    temp = {"Concealing Baby Swallow": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Concealing Baby Swallow'].append(data['time'][ind])
    if len(temp['Concealing Baby Swallow']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLCOUNTERATTACK(open, high, low, close)
    temp = {"Counterattack": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Counterattack'].append(data['time'][ind])
    if len(temp['Counterattack']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
    temp = {"Dark Cloud Cover": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Dark Cloud Cover'].append(data['time'][ind])
    if len(temp['Dark Cloud Cover']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLDOJI(open, high, low, close)
    temp = {"Doji": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Doji'].append(data['time'][ind])
    if len(temp['Doji']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLDOJISTAR(open, high, low, close)
    temp = {"Doji Starn": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Doji Star'].append(data['time'][ind])
    if len(temp['Doji Star']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLDRAGONFLYDOJI(open, high, low, close)
    temp = {"Harami": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Harami'].append(data['time'][ind])
    if len(temp['Harami']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLENGULFING(open, high, low, close)
    temp = {"Engulfing Pattern": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Engulfing Pattern'].append(data['time'][ind])
    if len(temp['Engulfing Pattern']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)
    temp = {"Evening Doji Star": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Evening Doji Star'].append(data['time'][ind])
    if len(temp['Evening Doji Star']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLEVENINGSTAR(open, high, low, close, penetration=0)
    temp = {" Evening Star": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp[' Evening Star'].append(data['time'][ind])
    if len(temp[' Evening Star']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLGAPSIDESIDEWHITE(open, high, low, close)
    temp = {"Up/Down-gap side-by-side white lines": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Up/Down-gap side-by-side white lines'].append(data['time'][ind])
    if len(temp['Up/Down-gap side-by-side white lines']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLGRAVESTONEDOJI(open, high, low, close)
    temp = {"Gravestone Doji": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Gravestone Doji'].append(data['time'][ind])
    if len(temp['Gravestone Doji']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLHAMMER(open, high, low, close)
    temp = {"Hammer": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Hammer'].append(data['time'][ind])
    if len(temp['Hammer']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLHANGINGMAN(open, high, low, close)
    temp = {"Hanging Man": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Hanging Man'].append(data['time'][ind])
    if len(temp['Hanging Man']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLHARAMI(open, high, low, close)
    temp = {"Harami Pattern": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Harami Pattern'].append(data['time'][ind])
    if len(temp['Harami Pattern']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLHARAMICROSS(open, high, low, close)
    temp = {"Harami Cross Pattern": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Harami Cross Pattern'].append(data['time'][ind])
    if len(temp['Harami Cross Pattern']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLHIGHWAVE(open, high, low, close)
    temp = {"High-Wave Candle": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['High-Wave Candle'].append(data['time'][ind])
    if len(temp['High-Wave Candle']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLHIKKAKE(open, high, low, close)
    temp = {"Hikkake Pattern": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Hikkake Pattern'].append(data['time'][ind])
    if len(temp['Hikkake Pattern']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLHIKKAKEMOD(open, high, low, close)
    temp = {"Modified Hikkake Pattern": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Modified Hikkake Pattern'].append(data['time'][ind])
    if len(temp['Modified Hikkake Pattern']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLHOMINGPIGEON(open, high, low, close)
    temp = {"Homing Pigeon": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Homing Pigeon'].append(data['time'][ind])
    if len(temp['Homing Pigeon']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLIDENTICAL3CROWS(open, high, low, close)
    temp = {"Identical Three Crows": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Identical Three Crows'].append(data['time'][ind])
    if len(temp['Identical Three Crows']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLINNECK(open, high, low, close)
    temp = {"In-Neck Pattern": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['In-Neck Pattern'].append(data['time'][ind])
    if len(temp['In-Neck Pattern']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLINVERTEDHAMMER(open, high, low, close)
    temp = {"Inverted Hammer": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Inverted Hammer'].append(data['time'][ind])
    if len(temp['Inverted Hammer']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLKICKING(open, high, low, close)
    temp = {"Kicking": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Kicking'].append(data['time'][ind])
    if len(temp['Kicking']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLKICKINGBYLENGTH(open, high, low, close)
    temp = {"Kicking - bull/bear": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Kicking - bull/bear'].append(data['time'][ind])
    if len(temp['Kicking - bull/bear']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLLADDERBOTTOM(open, high, low, close)
    temp = {"Ladder Bottom": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Ladder Bottom'].append(data['time'][ind])
    if len(temp['Ladder Bottom']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLLONGLEGGEDDOJI(open, high, low, close)
    temp = {"Long Legged Doji": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Long Legged Doji'].append(data['time'][ind])
    if len(temp['Long Legged Doji']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLLONGLINE(open, high, low, close)
    temp = {"Long Line Candle": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Long Line Candle'].append(data['time'][ind])
    if len(temp['Long Line Candle']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLMARUBOZU(open, high, low, close)
    temp = {"Marubozu": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Marubozu'].append(data['time'][ind])
    if len(temp['Marubozu']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLMATCHINGLOW(open, high, low, close)
    temp = {"Matching Low": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Matching Low'].append(data['time'][ind])
    if len(temp['Matching Low']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLMATHOLD(open, high, low, close, penetration=0)
    temp = {"Mat Hold": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Mat Hold'].append(data['time'][ind])
    if len(temp['Mat Hold']) > 0:
        final_list[eqname].append(temp)

    integer = t.CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)
    temp = {"Morning Doji Star": []}
    for ind, i in enumerate(integer):
        if i != 0:
            temp['Morning Doji Star'].append(data['time'][ind])
    if len(temp['Morning Doji Star']) > 0:
        final_list[eqname].append(temp)
    return final_list


