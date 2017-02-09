import pandas as pd

#ME-1 Thread Freeze
# normal_file = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\ME-1 Thread Freeze\\Normal_Matching_1_1_MatchingEngine_1.csv"
# anomalous_file = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\ME-1 Thread Freeze\\Abnormal_ME_1_THREAD_FREEZE_PT0_times.csv"
# output_csv = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\ME-1 Thread Freeze\\ME-1.csv"

#NG-1 Real Thread Freeze
# normal_file = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\NG-1 Real Thread Freeze\\Normal_Native_1_1_NativeGateway_1.csv"
# anomalous_file = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\NG-1 Real Thread Freeze\\Abnormal_NG_1_THREAD_FREEZE_MAIN_times.csv"
# output_csv = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\NG-1 Real Thread Freeze\\NG-1.csv"

#NG-2
# normal_file = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\NG-2 Kill Start\\Normal_Native_1_1_NativeGateway_2.csv"
# anomalous_file = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\NG-2 Kill Start\\Abnormal_NG_2_WSR1_times.csv"
# output_csv = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\NG-2 Kill Start\\NG-2.csv"

#SEQ
normal_file = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\SEQ-1 IO\\Normal_Matching_1_1_Sequencer_1.csv"
anomalous_file = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\SEQ-1 IO\\Abnormal_SQ_1_THREAD_FREEZE_DISKWRITER_times.csv"
output_csv = "D:\\Semester 7\\FYP\\DataSet\\Dataset - Phase 3\\Loch P3\\SEQ-1 IO\\SEQ-1.csv"

unformatted_normal = pd.read_csv(normal_file,keep_default_na=False, na_values=[""])
abnormal = pd.read_csv(anomalous_file,keep_default_na=False, na_values=[""])


def format_normal_data(df):
    df['Status'] = '0'
    df.to_csv(normal_file, index=False)
    return

def concat_data(df1, df2):
    vertical_stack = pd.concat([df1, df2], axis=0)
    vertical_stack.to_csv(output_csv, index=False)



format_normal_data(unformatted_normal)
normal = pd.read_csv(normal_file,keep_default_na=False, na_values=[""])
concat_data(normal,abnormal)
