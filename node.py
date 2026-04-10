class ScenePromptNode:
    """Background + two characters with poses. Large text inputs for clear visibility."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "background_mood_atmosphere": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Background (mood/atmosphere): e.g. dimly lit hotel room at midnight, city skyline through windows",
                }),
                "vibe_optional": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Vibe (optional): e.g. tense, romantic, dreamy",
                }),
                "character_1_description": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Character 1 description: e.g. young woman, dark hair, blue eyes",
                }),
                "character_1_pose_and_action": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Character 1 pose & action: e.g. all fours on silk sheets, back arched dramatically",
                }),
                "character_2_description": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Character 2 description: e.g. Mediterranean woman, platinum pixie cut, blue eyes",
                }),
                "character_2_pose_and_action": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "placeholder": "Character 2 pose & action: e.g. kneeling beside her, hand on her shoulder",
                }),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "background", "character_1", "character_2")
    FUNCTION = "run"
    CATEGORY = "fusefree"

    def run(
        self,
        background_mood_atmosphere="",
        vibe_optional="",
        character_1_description="",
        character_1_pose_and_action="",
        character_2_description="",
        character_2_pose_and_action="",
    ):
        parts = []
        if background_mood_atmosphere.strip():
            parts.append(f"A picture of two characters, {background_mood_atmosphere.strip()}")
        if vibe_optional.strip():
            parts.append(vibe_optional.strip())
        if character_1_description.strip():
            parts.append(f"The first character is {character_1_description.strip()}")
        if character_1_pose_and_action.strip():
            parts.append(character_1_pose_and_action.strip())
        if character_2_description.strip():
            parts.append(f"The second character is {character_2_description.strip()}")
        if character_2_pose_and_action.strip():
            parts.append(character_2_pose_and_action.strip())
        prompt = " ".join(parts) if parts else ""
        background_raw = background_mood_atmosphere.strip()
        char_1_raw = character_1_description.strip()
        char_2_raw = character_2_description.strip()
        return (prompt, background_raw, char_1_raw, char_2_raw)
