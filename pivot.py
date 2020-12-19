import pandas as pd
file_path = "CA1\states_all_extended_cleaned.csv"

original_df = pd.read_csv(file_path)
primary_key, state, year, race, Grade_1, Grade_2, Grade_3, Grade_4, Grade_5, Grade_6, Grade_7, Grade_8, Grade_9, Grade_10, Grade_11, Grade_12, Kindergarden, Pre_Kindergarden, NAEP_Grade_4_Math, NAEP_Grade_4_Reading, NAEP_Grade_8_Math, NAEP_Grade_8_Reading,  = [
], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

# races = {
#     "WH" : {
#         "Enrolment Columns" : []
#     }
# }
# df_copy = original_df.copy()[:500]

races = ['WH', 'BL', 'HI', 'AS', 'AM', 'HP', 'TR']
for idx, row in original_df.iterrows():
    for race_id in races:
        primary_key.append(row["PRIMARY_KEY"] + '_' + race_id)
        year.append(row["YEAR"])
        # for gender in ['M', 'F']:
        race.append(race_id)
        state.append(row['STATE'])
        Grade_1.append(row['G01_{}_M'.format(race_id)] +
                       row['G01_{}_F'.format(race_id)])
        Grade_2.append(row['G02_{}_M'.format(race_id)] +
                       row['G02_{}_F'.format(race_id)])
        Grade_3.append(row['G03_{}_M'.format(race_id)] +
                       row['G03_{}_F'.format(race_id)])
        Grade_4.append(row['G04_{}_M'.format(race_id)] +
                       row['G04_{}_F'.format(race_id)])
        Grade_5.append(row['G05_{}_M'.format(race_id)] +
                       row['G05_{}_F'.format(race_id)])
        Grade_6.append(row['G06_{}_M'.format(race_id)] +
                       row['G06_{}_F'.format(race_id)])
        Grade_7.append(row['G07_{}_M'.format(race_id)] +
                       row['G07_{}_F'.format(race_id)])
        Grade_8.append(row['G08_{}_M'.format(race_id)] +
                       row['G08_{}_F'.format(race_id)])
        Grade_9.append(row['G09_{}_M'.format(race_id)] +
                       row['G09_{}_F'.format(race_id)])
        Grade_10.append(row['G10_{}_M'.format(race_id)] +
                        row['G10_{}_F'.format(race_id)])
        Grade_11.append(row['G11_{}_M'.format(race_id)] +
                        row['G11_{}_F'.format(race_id)])
        Grade_12.append(row['G12_{}_M'.format(race_id)] +
                        row['G12_{}_F'.format(race_id)])
        Kindergarden.append(row['KG_{}_M'.format(
            race_id)]+row['KG_{}_F'.format(race_id)])
        Pre_Kindergarden.append(row['PK_{}_M'.format(
            race_id)]+row['PK_{}_F'.format(race_id)])
        NAEP_Grade_4_Math.append(row['G04_{}_A_MATHEMATICS'.format(race_id)])
        NAEP_Grade_4_Reading.append(row['G04_{}_A_READING'.format(race_id)])
        NAEP_Grade_8_Math.append(row['G08_{}_A_MATHEMATICS'.format(race_id)])
        NAEP_Grade_8_Reading.append(row['G08_{}_A_READING'.format(race_id)])

output = pd.DataFrame({
    'PRIMARY KEY': primary_key,
    'State': state,
    'Year': year,
    'Race': race,
    'Grade 1': Grade_1,
    'Grade 2': Grade_2,
    'Grade 3': Grade_3,
    'Grade 4': Grade_4,
    'Grade 5': Grade_5,
    'Grade 6': Grade_6,
    'Grade 7': Grade_7,
    'Grade 8': Grade_8,
    'Grade 9': Grade_9,
    'Grade 10': Grade_10,
    'Grade 11': Grade_11,
    'Grade 12': Grade_12,
    'Kindergarden': Kindergarden,
    'Pre Kindergarden': Pre_Kindergarden,
    'NAEP Grade 4 Math': NAEP_Grade_4_Math,
    'NAEP Grade 4 Reading': NAEP_Grade_4_Reading,
    'NAEP Grade 8 Math': NAEP_Grade_8_Math,
    'NAEP Grade 8 Reading': NAEP_Grade_8_Reading
}).to_csv('test_output_3-16-11-2020.csv')
