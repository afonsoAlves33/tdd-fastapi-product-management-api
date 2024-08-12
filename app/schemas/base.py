from pydantic import BaseModel


class CustomBaseModel(BaseModel): # BaseModel is the pydantic base for serializing your models
    def dict(*args, **kwargs):
        d = super().dict(*args, **kwargs)
        filtered_dict = {k: v for k, v in d.items() if v is not None} # checks keys and values in the dict and deletes from the dict keys with valus of type None
        return filtered_dict
  