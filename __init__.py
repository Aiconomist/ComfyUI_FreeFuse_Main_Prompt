from .node import ScenePromptNode

NODE_CLASS_MAPPINGS = {
    "ScenePromptNode": ScenePromptNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ScenePromptNode": "FuseFree Main Prompt",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
