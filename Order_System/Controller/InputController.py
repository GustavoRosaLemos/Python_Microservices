import os
import string
from Model import StatusModel
sm = StatusModel
from dotenv import load_dotenv
load_dotenv()

class InputControl:
    def verify_auth(self, req:dict) -> bool:
        try:
            req['auth']
        except:
            return False
        if not req['auth'] == os.getenv('AUTH_KEY'): return False
        return True

    def verify_order_requeriments(self, req:dict) -> sm:
        try:
            req['user_id']
            req['item_description']
            req['item_quantity']
            req['item_price']
        except:
            return sm.StatusModel("Error: json need has (user_id, item_description, item_quantity, item_price)", 400)
        if not self.verify_item_quantity(req['item_quantity']): return sm.StatusModel("Error: Invalid item_quantity!", 400)
        if not self.verify_item_price(req['item_price']): return sm.StatusModel("Error: Invalid item_price!", 400)
    
    def verify_generated_requeriments(self, req:dict) -> sm:
        try:
            req['id']
            req['updated_at']
            req['total_value']
        except:
            return sm.StatusModel("Error: cannot get (id, update_at or total_value) generated by server", 500)
        if not self.verify_total_value(req['total_value']): return sm.StatusModel("Error: Invalid total_value!", 400)

    def verify_item_quantity(self, item_quantity:(str, int)) -> bool:
        try:
            int(item_quantity)
        except:
            return False
        return True
    
    def verify_item_price(self, item_price:(str, int, float)) -> bool:
        try:
            float(item_price)
        except:
            return False
        return True
    
    def verify_total_value(self, total_value:(str, int, float)) -> bool:
        try:
            float(total_value)
        except:
            return False
        return True

    def verify_id(self, req:dict) -> bool:
        try:
            req['id']
        except:
            return False
        return True

        