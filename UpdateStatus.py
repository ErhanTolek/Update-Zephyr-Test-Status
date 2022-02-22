    def JiraStatus(self, IssueKey, STATUS):
        

        def GetIssueId(IssueKey, STATUS):
            import requests
            headers = {
                "Accept": "application/json",
                'Content-Type': 'application/json'
            }
            response = requests.get(f'##################{IssueKey}###############',
                                    headers=########, auth=("#########", "############"))
            data = response.json()
            IssueId = data['id']
            GetExecutionId(IssueId, 126, f'{STATUS}')

        def changeExecutionStatus(statusValue, executionId):
            import requests
            values = f'{{"status": "{statusValue}" }}'
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.put(f'#####################################{executionId}#########
                                    data=####, headers=#######, auth=(#######, #########))

        def GetExecutionId(IssueId, CycleId, STATUS):
            import requests
            import json
            headers = {
                "Accept": "application/json",
                'Content-Type': 'application/json'
            }
            response = requests.get(
                f'#####################################{IssueId}#########{CycleId}
                                    data=####, headers=#######, auth=(#######, #########)))
            data1 = response.json()
            json.dumps(data1)
            executionId = json.dumps(data1['executions'][0]['id'])
            changeExecutionStatus(f'{STATUS}', executionId)

        GetIssueId(f'{IssueKey}', f'{STATUS}')
