import os
import re
import folder_paths

class ColorCSVLoader:
    ...
    
    @staticmethod
    def load_color_csv():
        """Loads csv file with colorstyles from a subdirectory called 'csv'.
        ...
        """
        # Construct the path to the 'color.csv' file within the 'csv' subdirectory
        color_path = os.path.join(folder_paths.base_path, "app/data", "color.csv")
        
        colorstyles = {"Error loading color.csv, check the console": ["",""]}
        if not os.path.exists(color_path):
            print(f"""Error. No color.csv found in the 'csv' subdirectory. Put your color.csv in the 'csv' folder within the root directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return colorstyles
        try:
            with open(color_path, "r", encoding="utf-8") as f:
                lines = [[x.replace('"', '').replace('\n', '') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                colorstyles = {x[0]: [x[1], x[2]] for x in lines}
        except Exception as e:
            print(f"""Error loading color.csv from the 'csv' subdirectory. Make sure it is in the 'csv' folder within the root directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return colorstyles
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.color_csv = cls.load_color_csv()
        return {
            "required": {
                "colorstyles": (list(cls.color_csv.keys()),),
            },                          
        }
    
    RETURN_TYPES = ("STRING", "STRING")  # Expecting two string outputs now
    RETURN_NAMES = ("positive_prompt", "negative_prompt")  # Naming the outputs


    FUNCTION = "execute"
    CATEGORY = "loaders"

    def execute(self, colorstyles):
        # Return both the positive and negative prompts for the given style
        return (self.color_csv[colorstyles][0], self.color_csv[colorstyles][1])

NODE_CLASS_MAPPINGS = {
    "Load Color CSV": ColorCSVLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ColorCSVLoader": "Load Color CSV Node"
}
