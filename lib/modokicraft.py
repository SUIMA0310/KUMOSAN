import subprocess

# send some signals to Modokicraft
def send_signal_to_modokicraft(text):
    response_string = ''
    if text.find("modokicraft kick") > -1:
        index_st = text.find('kick ') + 5
        #index_ed = text.find('')
        user_name = text[index_st:]
        response_string = "了解いたしました。"+ user_name + "さんをキックします。"
        try:
            subprocess.call(["sh", "modokicraft_scripts/kick.sh", user_name])
        except Exception as e:
            response_string = '構文エラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
        '''
    elif text == "雲さん modokicraft restart":
        response_string = "了解いたしました。もどくらを再起動します。"
        #スクリーン及び起動スクリプトへのkillコマンド挿入
        try:
            subprocess.call(["sh", "modokicraft_scripts/quit.sh"])
        except Exception as e:
            response_string = '構文エラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
        #スクリーン及び起動スクリプトの実行コマンド挿入
        try:
            subprocess.call(["sh", "modokicraft_scripts/restart.sh"])
        except Exception as e:
            response_string = '構文エラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
        '''
    else:
        response_string = "構文エラーです＞＜ :cold_sweat:\n 正しく入力してね！"

    return response_string
