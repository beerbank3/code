def weekly_data_to_excel(startdate,enddate,data):
    
    excel_file = load_workbook('weekly_sample.xlsx')

    sheet1 = excel_file['금주']

    print(sheet1)
    worksheet1_table_key = ["date","dayofweek","week","pcMblTp","campaignTp","campaignname","keyword","impCnt","clkCnt","salesAmt","ccnt","convAmt"]
    row = 2
    for i,keyword in enumerate(data['key_temp_report']):
        for index, value in enumerate(value for key, value in keyword.items() if key in worksheet1_table_key):
            sheet1.cell(row, index+1,value)
        row += 1

    # excel 파일 bytesIO로 저장
    
    with NamedTemporaryFile() as tmp:
        excel_file.save(tmp)
        tmp.seek(0)
        stream = tmp.read()

    # Set up the Http response.
    today = datetime.today().strftime('%Y%m%d')
    filename = 'weekly_report' + '_' + today + '.xlsx'
    response = HttpResponse(
        stream,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response["Content-Disposition"] = "attachment; filename=%s" % filename # 한글 제목 설정
    return response