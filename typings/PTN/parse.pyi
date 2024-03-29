"""
This type stub file was generated by pyright.
"""

class PTN:
    def __init__(self) -> None:
        ...
    
    def parse(self, name, standardise, coherent_types): # -> dict[Any, Any]:
        ...
    
    @staticmethod
    def normalise_pattern_options(pattern_options): # -> list[Any]:
        ...
    
    def get_matches(self, pattern, clean_name, key): # -> list[Any]:
        ...
    
    def ignore_before_index(self, clean_name, key): # -> Any | Literal[0]:
        ...
    
    @staticmethod
    def get_match_indexes(match): # -> dict[str, int]:
        ...
    
    @staticmethod
    def get_season_episode(match): # -> list[int] | int | None:
        ...
    
    @staticmethod
    def split_multi(match): # -> list[Any]:
        ...
    
    @staticmethod
    def get_subtitles(match): # -> list[Any]:
        ...
    
    def standardise_clean(self, clean, key, replace, transforms): # -> list[Any] | Any | Literal['Available']:
        ...
    
    @staticmethod
    def standardise_languages(clean): # -> list[Any]:
        ...
    
    @staticmethod
    def standardise_genres(clean): # -> list[Any]:
        ...
    
    def merge_match_slices(self): # -> None:
        ...
    
    def process_title(self): # -> None:
        ...
    
    def unmatched_list(self, keep_punctuation=...): # -> list[Any]:
        ...
    
    def fix_known_exceptions(self): # -> None:
        ...
    
    def get_unmatched(self): # -> Literal['']:
        ...
    
    def clean_unmatched(self): # -> list[Any]:
        ...
    


