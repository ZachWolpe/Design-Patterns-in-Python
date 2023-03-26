
# ========================================================================
# File: bridge.py
# 
# Objective: Implement the bridge design pattern.
#
# Description: Suppose we write the code to flight navigation software for 
# the Lockhead Martin. For a given plan, need a class that implements a 
# number of flight & defence functions. As the number of planes & variants 
# grows, the number of combinations grows exponentially, the bridge allows 
# us to decouple the pairing between variants. The `Attack` class is 
# abstracted & passed to the `FighterJet` class.
#
# ------------------------------------------------------------------------
# author:         zach wolpe
# email:          zach.wolpe@medibio.com.au
# date:           13.03.23
# ========================================================================


class Attack:
    def attack_stategy(self):
        pass

class AttackStategy1(Attack):
    def attack_stategy(self):
        print('Executing attack strategy 1.')

class AttackStategy2(Attack):
    def attack_stategy(self):
        print('Executing attack strategy 2.')


class FighterJet:
    def __init__(self, attack) -> None:
        self.attack = attack
    
    def flight_navigator(self):
        pass

    def launch_attack(self):
        self.attack.attack_stategy()



class F35(FighterJet):
    def __init__(self, attack) -> None:
        super().__init__(attack)

    def flight_navigator(self):
        return super().flight_navigator()
    
    def launch_attack(self):
        return super().launch_attack()




if __name__ == '__main__':
    strategy_1 = AttackStategy1()
    strategy_2 = AttackStategy2()
    f35 = F35(strategy_1)
    MIG = F35(strategy_2)
    f35.launch_attack()
    MIG.launch_attack()



