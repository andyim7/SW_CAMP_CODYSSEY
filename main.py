try:
    # 로그 파일 열기 (UTF-8)
    with open('mission_computer_main.log','r', encoding='utf8') as file:
        log_content = file.read()
        print(log_content)
    
    # 로그 분석 보고서 (Markdown) 파일 저장
    with open('log_analysis.md','w',encoding='utf8') as report:
        report.write('# Log Analysis\n\n')
        report.write('## 사고 요약\n')
        report.write('- 산소탱크 불안정 -> 5분 후 폭발 \n')
        report.write('## 로그 요약\n')
        report.write('```\n')
        report.write('2023-08-27 11:35:00,INFO,Oxygen tank unstable.\n')
        report.write('2023-08-27 11:40:00,INFO,Oxygen tank explosion.\n')
        report.write('```\n\n')
        report.write('## 결론\n')
        report.write('- 산소탱크 압력 이상을 조기에 감지하고 자동 벤트 시스템 필요.\n')

    print('\n 분석 결과를 log_analysis.md 파일에 저장했습니다')

    # 예외 처리
except FileNotFoundError:
    print('로그 파일을 찾을 수 없습니다. 파일 이름과 위치를 확인하세요.')
except UnicodeDecodeError:
    print('로그 파일을 UTF-8로 읽는데 실패했습니다. 인코딩을 확인하세요.')
except Exception as e:
    print('알 수 없는 오류가 발생했습니다:', e)