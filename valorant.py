import requests
import json
import re
import datetime
import time


class ValorantAPI:
    def __init__(self, username, tag, region="eu", language="en-us"):
        self.username, self.tag, self.region, self.language = username, tag, region, language
        self.session = requests.Session()
        self.base_endpoint = "https://ayberkenis.com.tr/api/v1/valorant/"
        with open('translations.json', 'r', encoding='utf-8') as file:
            self.languages = json.load(file)

    def get(self, endpoint, *args):
        r = self.session.get(self.base_endpoint + endpoint, *args)
        return r.json()

    def get_mmr_info(self):
        rank = self.get(f"mmr/{self.username}/{self.tag}/{self.region}")
        return self.get_translation('rank', rank, self.language)

    def get_last_match(self):
        start = time.time()
        match = self.get(f"match/latest/{self.username}/{self.tag}/{self.region}")
        print(f"Time taken to get last match: {time.time() - start}")
        return self.get_translation('match', match, self.language)

    def get_translation(self, endpoint, data, language):
        start = time.time()
        text = self.languages[language][endpoint]
        _all_ = re.findall(r"\$\([^)]*\)", text)
        if endpoint == 'rank':
            for i in _all_:
                text = text.replace(i, str(data[i[2:-1]]))
        elif endpoint == 'match':
            try:
                for i in _all_:
                    text = text.replace(i, str(data[i[2:-1]]))
            except KeyError:
                repl = self.build_match_replacements(data)
                _repl_ = re.findall(r"\$\([^)]*\)", text)
                for i in _repl_: text = text.replace(i, str(repl[i]))
        print(f"Time taken: {time.time() - start}")
        return text

    def build_match_replacements(self, data) -> dict:
        match_score = f"{data['Match']['self_player']['rounds_won']} - {data['Match']['self_player']['rounds_lost']}"
        match_result = self.languages[self.language]['won'] if data['Match']['self_player']['won'] else self.languages[self.language]['lost']
        server = data['Match']['match_info']['server']
        map = data['Match']['match_info']['map_name']
        minutes = datetime.datetime.fromtimestamp(data['Match']['match_info']['game_length']).minute
        seconds = datetime.datetime.fromtimestamp(data['Match']['match_info']['game_length']).second
        data = data['Match']
        headshot_rate = data['self_player']['total_damage']['total_headshots'] / (data['self_player']['total_damage']['total_bodyshots'] + data['self_player']['total_damage']['total_headshots'] + data['self_player']['total_damage']['total_legshots'])
        return {'$(currentplayer)': self.username, '$(match_score)': match_score,
                '$(last_match_rr)': data['self_player']['last_match_rr'],
                '$(match_result)': match_result,
                '$(server)': server.capitalize(), '$(map)': map, '$(match_length)': f"{minutes}:{seconds}",
                '$(minutes)': minutes,
                '$(seconds)': seconds,
                '$(kills)': data['self_player']['kills'], '$(deaths)': data['self_player']['deaths'],
                '$(assists)': data['self_player']['assists'],
                '$(total_bodyshots)': data['self_player']['total_damage']['total_bodyshots'],
                '$(total_headshots)': data['self_player']['total_damage']['total_headshots'],
                '$(headshot_rate)': round(headshot_rate, 2),
                '$(total_damage)': data['self_player']['total_damage']['total_damage']}
