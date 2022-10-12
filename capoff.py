import numpy as np
import pandas as pd
import math

xls = pd.ExcelFile("miscellenious_discounts/input_files/input_price_module_discounts.xlsm")
parameters_df = pd.read_excel(xls, "Parameters")
parameters = parameters_df.to_numpy()


def capoff_prem(premiums):
    def getPos(x):
        ans = 0
        if len(x) >= 1:
            ans += 26 * (len(x) - 1)
        return ans + (ord(x[-1]) - ord("A"))

    upperMaxima = parameters[17:25, getPos("AE"):getPos("AH") + 1]

    upperMaxima[0, 1] = "Individual Maxima"
    upperMaxima[0, 2] = "Group Maxima"
    upperMaxima[0, 3] = "Total Maxima"

    def toDataFrame(nparr: np.array):
        nparrdf = pd.DataFrame(list(nparr))
        nparrdf.columns = nparrdf.iloc[0]
        nparrdf = nparrdf.drop(nparrdf.index[0])
        return nparrdf

    upperMaximadf = toDataFrame(upperMaxima)

    upperMaximadf["Group Maxima"] = upperMaximadf["Group Maxima"].fillna(
        method="ffill")
    upperMaximadf["Total Maxima"] = upperMaximadf["Total Maxima"].fillna(
        method="ffill")
    upperMaximadf["Group Maxima"] = upperMaximadf["Group Maxima"] * 100
    upperMaximadf["Total Maxima"] = upperMaximadf["Total Maxima"] * 100
    upperMaximadf["Individual Maxima"] = upperMaximadf["Individual Maxima"] * 100

    def capPremiumsIndividual(property_name, property_premium, premium_df):
        property_premium = min(
            property_premium, premium_df[premium_df["Grading"] == property_name]["Individual Maxima"].values[0])
        return property_premium

    def capPremiumsGroup(property_group, group_premiums, premium_df):
        for i in range(len(premium_df["Grading"])):
            premium_df["Grading"].values[i] = premium_df["Grading"].values[i].strip()

        premium_sum = 0
        for i in range(len(group_premiums)):
            premium_sum += group_premiums[i]

        premium_sum = min(
            premium_sum, premium_df[premium_df["Grading"] == property_group[0]]["Group Maxima"].values[0])
        return premium_sum

    def capPremiumsTotal(properties, premiums, premium_df):
        total_premiums = 0
        for i in range(len(properties)):
            total_premiums += premiums[i]
        if not math.isnan(premium_df["Total Maxima"].values[0]):
            # print(premium_df["Total Maxima"].values[0])
            total_premiums = min(total_premiums, premium_df["Total Maxima"].values[0])
        else:
            total_premiums = 999999
        return total_premiums

    def capPremiumsOneUp(properties, premiums, premium_df):
        # capping off individual premiums
        for i in range(len(premiums)):
            premiums[i] = capPremiumsIndividual(
                properties[i], premiums[i], premium_df)

        # creating groups according to sheet
        grp1 = properties[0:3]
        grp2 = properties[3:7]

        grp1_prem = premiums[0:3]
        grp2_prem = premiums[3:7]
        # print(grp1_prem)
        # print(grp2_prem)

        # capping off group premiums
        grp1_prem = capPremiumsGroup(grp1, grp1_prem, premium_df)
        grp2_prem = capPremiumsGroup(grp2, grp2_prem, premium_df)

        # capping off total premiums
        total_prem = capPremiumsTotal(properties, premiums, premium_df)
        # print(total_prem)

        return min(total_prem, grp1_prem + grp2_prem)

    # # testcase for one up discount capoff
    properties = upperMaximadf["Grading"].values
    # premiums = [2, 3, 1, 0, 0, 0, 0]
    # premiums = premiums[::-1]

    return capPremiumsOneUp(properties, premiums, upperMaximadf)


def capoff_discounts(discounts, basic):
    def getPos(x):
        ans = 0
        if len(x) >= 1:
            ans += 26 * (len(x) - 1)
        return ans + (ord(x[-1]) - ord("A"))

    lowerMaxima = parameters[0:14, getPos("AE"):getPos("AH") + 1]

    lowerMaxima[0, 1] = "Individual Maxima"
    lowerMaxima[0, 2] = "Group Maxima"
    lowerMaxima[0, 3] = "Total Maxima"

    def toDataFrame(nparr: np.array):
        nparrdf = pd.DataFrame(list(nparr))
        nparrdf.columns = nparrdf.iloc[0]
        nparrdf = nparrdf.drop(nparrdf.index[0])
        return nparrdf

    lowerMaximadf = toDataFrame(lowerMaxima)

    lowerMaximadf["Group Maxima"] = lowerMaximadf["Group Maxima"].fillna(
        method="ffill")
    lowerMaximadf["Total Maxima"] = lowerMaximadf["Total Maxima"].fillna(
        method="ffill")
    lowerMaximadf["Group Maxima"] = lowerMaximadf["Group Maxima"] * 100
    lowerMaximadf["Total Maxima"] = lowerMaximadf["Total Maxima"] * 100
    lowerMaximadf["Individual Maxima"] = lowerMaximadf["Individual Maxima"] * 100

    def capDiscountIndividual(property_name, property_discount, discount_df):
        property_discount = max(
            property_discount, discount_df[discount_df["Grading"] == property_name]["Individual Maxima"].values[0])
        return property_discount

    def capDiscountGroup(property_group, group_discount, discount_df):
        for i in range(len(discount_df["Grading"])):
            discount_df["Grading"].values[i] = discount_df["Grading"].values[i].strip()

        discount_sum = 0
        for i in range(len(group_discount)):
            discount_sum += group_discount[i]
        # print(discount_df[discount_df["Grading"] ==
        #       property_group[1]]["Group Maxima"].values)
        # print(property_group)
        # print(discount_df[discount_df["Grading"] ==
        #       property_group[0]]["Group Maxima"].values)
        # print(property_group[0])
        for i in range(len(property_group)):
            if len(discount_df[discount_df["Grading"] == property_group[i]]["Group Maxima"].values) > 0:
                temp = discount_df[discount_df["Grading"] ==
                                   property_group[i]]["Group Maxima"].values[0]
                break
            else:
                temp = 0
        discount_sum = max(
            discount_sum, temp)
        return discount_sum

    def capDiscountTotal(properties, discounts, discount_df):
        totalDiscount = 0
        for i in range(len(properties)):
            totalDiscount += discounts[i]
        totalDiscount = max(totalDiscount, discount_df["Total Maxima"].values[0])
        return totalDiscount

    def capDiscountsOneUp(properties, discounts, discount_df, basic):
        # capping off individual discounts
        for i in range(len(discounts)):
            discounts[i] = capDiscountIndividual(
                properties[i], discounts[i], discount_df)

        # creating groups according to sheet
        grp1 = properties[0:2]
        grp2 = properties[2:7]
        grp3 = properties[7:13]

        grp1_dis = discounts[0:2]
        grp2_dis = discounts[2:7]
        grp3_dis = discounts[7:13]

        # capping off group discounts
        grp1_dis = capDiscountGroup(grp1, grp1_dis, discount_df)
        grp2_dis = capDiscountGroup(grp2, grp2_dis, discount_df)
        grp3_dis = capDiscountGroup(grp3, grp3_dis, discount_df)

        # capping off total discounts
        total_dis = capDiscountTotal(properties, discounts, discount_df)

        return capDiscountDossiers(basic, max(total_dis, grp1_dis + grp2_dis + grp3_dis))

    def capDiscountDossiers(total_basic_dis, total_internal_dis):
        # basic is a list of numbers: basic discounts
        # internal is also a list of numbers: internal gradings discounts

        if total_basic_dis < -40:
            total_internal_dis = max(-20, total_internal_dis)
        else:
            total_internal_dis = max(-15, total_internal_dis)

        return total_internal_dis

    # testcase for one up discount capoff
    properties = lowerMaximadf["Grading"].values
    # print(properties)
    # discounts = [-2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14]
    # discounts = discounts[::-1]

    return capDiscountsOneUp(properties, discounts, lowerMaximadf, basic)
