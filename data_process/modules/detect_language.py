# `Language` is a class from the `lingua` library that represents a language. It is
# used in the `detect_language` function to specify the languages to be detected by
# the language detector.
from lingua import  Language, LanguageDetectorBuilder
# https://pypi.org/project/lingua-language-detector/


LANGUAGE_CODES ={
'AFRIKAANS': 'af',
'ALBANIAN': 'sq',
'ARABIC': 'ar',
'ARMENIAN': 'hy',
'AZERBAIJANI': 'az',
'BASQUE': 'eu',
'BELARUSIAN': 'be',
'BENGALI': 'bn',
'BOKMAL': 'nb',
'BOSNIAN': 'bs',
'BULGARIAN': 'bg',
'CATALAN': 'ca',
'CHINESE': 'zh',
'CROATIAN': 'hr',
'CZECH': 'cs',
'DANISH': 'da',
'DUTCH': 'nl',
'ENGLISH': 'en',
'ESPERANTO': 'eo',
'ESTONIAN': 'et',
'FINNISH': 'fi',
'FRENCH': 'fr',
'GANDA': 'lg',
'GEORGIAN': 'ka',
'GERMAN': 'de',
'GREEK': 'el',
'GUJARATI': 'gu',
'HEBREW': 'he',
'HINDI': 'hi',
'HUNGARIAN': 'hu',
'ICELANDIC': 'is',
'INDONESIAN': 'id',
'IRISH': 'ga',
'ITALIAN': 'it',
'JAPANESE': 'ja',
'KAZAKH': 'kk',
'KOREAN': 'ko',
'LATIN': 'la',
'LATVIAN': 'lv',
'LITHUANIAN': 'lt',
'MACEDONIAN': 'mk',
'MALAY': 'ms',
'MAORI': 'mi',
'MARATHI': 'mr',
'MONGOLIAN': 'mn',
'NYNORSK': 'nn',
'PERSIAN': 'fa',
'POLISH': 'pl',
'PORTUGUESE': 'pt',
'PUNJABI': 'pa',
'ROMANIAN': 'ro',
'RUSSIAN': 'ru',
'SERBIAN': 'sr',
'SHONA': 'sn',
'SLOVAK': 'sk',
'SLOVENE': 'sl',
'SOMALI': 'so',
'SOTHO': 'st',
'SPANISH': 'es',
'SWAHILI': 'sw',
'SWEDISH': 'sv',
'TAGALOG': 'tl',
'TAMIL': 'ta',
'TELUGU': 'te',
'THAI': 'th',
'TSONGA': 'ts',
'TSWANA': 'tn',
'TURKISH': 'tr',
'UKRAINIAN': 'uk',
'URDU': 'ur',
'VIETNAMESE': 'vi',
'WELSH': 'cy',
'XHOSA': 'xh',
'YORUBA': 'yo',
'ZULU': 'zu'
} 



class LanguageDetector:
    __instance = None
    @classmethod
    def __getInstance(cls):
        if not LanguageDetector.__instance:
            LanguageDetector.__instance = LanguageDetector()
        return LanguageDetector.__instance
    
    @classmethod
    def instance(cls):
        if not cls.__instance:
            cls.__instance = LanguageDetector()
        return cls.__instance 
    
    def __init__(self):
        languages = list(Language.__members__.values())
        self.detector = LanguageDetectorBuilder.from_languages(*languages).build()
        
    def __call__(self, text):
        confidence_values = self.detector.compute_language_confidence_values(text)
        for language, value in confidence_values:
            code = LANGUAGE_CODES.get(language.name,'None')
            print(f"{code}: {value:.2f}")
            return code


if __name__ == '__main__':
    # print(detect_language('Hello, world!'))  # Prints 'en'
    # print(detect_language('您好,世界!'))   # Prints 'zh'
    # print(detect_language('Hola, mundo!'))   # Prints 'es'
    detector = LanguageDetector()
    detector('Hello, world!')
    detector('您好,世界!')
    detector('Hola, mundo!')
    
    detector1 = LanguageDetector.instance()
    detector2 = LanguageDetector.instance()
    assert detector1 is detector2  # Same instance
    