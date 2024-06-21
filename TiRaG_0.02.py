import random
import math
import os

os.system('cls' if os.name == 'nt' else 'clear')

seed = random.randint(0, 1000000)
seed = 123123
random.seed(seed)
print("seed: ", seed)

WM_height = 9
WM_width = 9

world_map = [[0 for _ in range(WM_width+1)] for _ in range(WM_height+1)]
river_map = [[0 for _ in range(WM_width+1)] for _ in range(WM_height+1)]
cities_map = [[0 for _ in range(WM_width+1)] for _ in range(WM_height+1)]
forest_map = [[0 for _ in range(WM_width+1)] for _ in range(WM_height+1)]

cities_names_1 = ["archom", "heron", "korol", "shet", "molen", "dol", "keromis", "menet", "poites", "kort", "Ardol", "Viron", "Gratos", "Zilon", "Klatan", "Lerin", "Morgat", "Nolis", "Raldor", "Seltor"]
cities_names_2 = ["-her", " olo", "en lor", "of moreg", " cade", "itir", " of elgel", "imer", "-Garde", "-Holm", "forg", "veld", "tes", "lin", "nor", "berg", "-dor", "-town"]

cities_list = []

first_names = ["Uruh", "Erdor", "Rahath", "Sbit", "Aramis", "Belgas", "Darven", "Ergis", "Zaras", "Kalis", "Laris", "Merdon", "Noris", "Oldrik"]
last_names = ["Der Horoh", "Or Ollen", "Meter of", "Doren", "Elten", "Haldor", "Yorven", "Karel", "Larden", "Mardor", "Noris", "Relton", "Teris"]

res_names = ["wood", "stone", "ore", "coal", "iron", "instruments", "food"]

def intinput(text, min_ = None, max_ = None, is_valid = False):
    while is_valid != True:
        try:
            value = int(input(text))
        except:
            print("invalid input")
            continue
        if min_ != None:
            if (min_ > value):
                print("invalid input")
                continue
        if max_ != None:
            if (max_ < value):
                print("invalid input")
                continue
        os.system('cls' if os.name == 'nt' else 'clear')
        is_valid = True
    return value

class production:
    def __init__(self, name, workhours, workers, workplaces, production, consumption):
        self.name = name
        self.workers = workers
        self.workhours = workhours
        self.workplaces = workplaces
        self.production = production
        self.consumption = consumption
        self.salary = 0
        self.quantity = 0
        
class building:
    def __init__(self, name, res, workhours, production):
        self.name = name
        self.res = res
        self.workhours = workhours
        self.production = production

class citizen:
    def __init__(self, fname, lname, city):
        self.fname = fname
        self.lname = lname
        self.city = city
        self.work = None
        self.production = None
        self.motivation = 1
        self.money = 0
        self.workhours = 240
        self.hunger = 0
        self.basic_needs = [0, 0, 0, 0, 0, 0, 5]
        self.second_needs = [0, 0, 0, 0, 0, 0, 0]

    def needs(self):
        for i in range(len(self.basic_needs)):
             if self.city.ResourceManagement.res_price[i] != 0:
                IHTC = min(math.trunc(self.money / self.city.ResourceManagement.res_price[i]), self.basic_needs[i], self.city.ResourceManagement.res[i])
                self.money -= IHTC * self.city.ResourceManagement.res_price[i]
                self.basic_needs[i] -= IHTC
        if (0 in self.basic_needs) != (len(self.basic_needs)):
            hunger += 1
        if hunger == 5:
            del self

        for i in range(len(self.second_needs)):
             if self.city.ResourceManagement.res_price[i] != 0:
                IHTC = min(math.trunc(self.money / self.city.ResourceManagement.res_price[i]), self.second_needs[i])
                self.money -= IHTC * self.city.ResourceManagement.res_price[i]
                self.second_needs[i] -= IHTC

class ResourceManagement:
    def __init__(self, res_names):
        self.res_names = res_names
        self.res = []
        self.res_consumption = []
        self.res_production = []
        self.res_price = []

        for _ in range(len(self.res_names)):
            self.res.append(0)
            self.res_consumption.append(0)
            self.res_production.append(0)
            self.res_price.append(0)

        sawmill_production =            production("sawmill",                5,  [], 5,  [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0])
        stone_mine_production =         production("stone mine",             10, [], 5,  [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0])
        iron_mine_production =          production("iron mine",              5,  [], 5,  [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3, 0])
        coal_mine_production =          production("coal mine",              10, [], 5,  [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 4, 0])
        forge_production =              production("forge",                  4,  [], 5,  [0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 3, 0, 2, 0])
        workshop_production =           production("workshop",               3,  [], 5,  [0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 3, 0])
        building_company =              production("building company",       20, [], 10, [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 5, 0])
        trading_post =                  production("trading post",           20, [], 5,  [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0])
        farm_production =               production("farm",                   10, [], 5,  [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 2, 0])
        
        wood_basic_production =         production("wood production",        10, [], 1,  [1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0,  0])
        stone_basic_production =        production("stone production",       15, [], 1,  [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0,  0])
        ore_basic_production =          production("ore production",         20, [], 1,  [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0,  0])
        coal_basic_production =         production("coal production",        15, [], 1,  [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0,  0])
        iron_basic_production =         production("iron production",        12, [], 1,  [0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 5, 0, 0,  0])
        instrumenst_basic_production =  production("instruments production", 20, [], 1,  [0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0,  0])
        building_basic =                production("basic building",         20, [], 1,  [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 10, 0])
        raw_food_basic_production =     production("food production",        20, [], 1,  [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 3,  0])

        sawmill_build =                 building("sawmill",                  [5],                      150,  sawmill_production)
        stone_mine_build =              building("stone mine",               [10, 5],                  300,  stone_mine_production)
        iron_mine_build =               building("iron mine",                [20, 10],                 450,  iron_mine_production)
        coal_mine_build =               building("coal mine",                [15, 5],                  300,  coal_basic_production)
        forge_build =                   building("forge",                    [40, 20,  0, 10],         600,  forge_production)
        workshop_build =                building("workshop",                 [50, 25,  0, 15],         750,  workshop_production)
        building_company_build =        building("building company",         [50, 100, 0, 30, 0, 20],  1000, building_company)
        trading_post_build =            building("trading post build",       [50, 20,  0, 0,  0, 5],   500,  trading_post)
        farm_build =                    building("farm",                     [15, 0,   0, 0,  0, 0],   300,  farm_production)
        
        self.basic_production = [wood_basic_production, stone_basic_production, ore_basic_production, coal_basic_production, iron_basic_production, instrumenst_basic_production, building_basic, raw_food_basic_production]
        self.advanced_production = [sawmill_production, stone_mine_production, iron_mine_production, coal_mine_production, forge_production, workshop_production, building_company, trading_post, farm_production]
        self.buildings = [sawmill_build, stone_mine_build, iron_mine_build, coal_mine_build, forge_build, workshop_build, building_company_build, trading_post_build, farm_build]

class city:
    def __init__(self, name, population, y, x, fnames, lnames, new_birth = []):
        self.name = name
        self.population = population
        self.x = x
        self.y = y
        self.new_birth = new_birth
        self.citizens = []
        for i in range(population):
            self.citizens.append(citizen(random.choice(fnames), random.choice(lnames), self.name))

        self.employed_citizens = []
        self.unemployed_citizens = self.citizens
        
        self.ResourceManagement = ResourceManagement(res_names)
        self.budget = 0

        self.in_build = False
        self.currently_building = None
        self.building_time = 0
        self.res_total = 0
        self.res_done = 0

    def upd_population(self):
        for i in range(len(self.new_birth)):
            if self.new_birth == 9:
                self.population += 1
                self.new_birth.pop(i)
            else:
                self.new_birth[i] += 1
        for i in range(self.population):
            if (random.randint(0, 20)) == 0:
                self.new_birth.append(0) 
                
    def new_citizen(self, fname, lname):
        self.citizens.append(citizen(fname, lname, self))
        self.population += 1
        
    def economics_upd(self):
        self.bbp = 0
        
        for i in range(len(self.ResourceManagement.res)):
            self.ResourceManagement.res[i] = self.ResourceManagement.res_production[i] - self.ResourceManagement.res_consumption[i]
            if self.ResourceManagement.res_production[i] != 0:
                self.ResourceManagement.res_price[i] = self.ResourceManagement.res_consumption[i] / self.ResourceManagement.res_production[i]
            else:
                self.ResourceManagement.res_price[i] = 0 
            self.bbp += self.ResourceManagement.res_price[i] * self.ResourceManagement.res_consumption[i] + self.ResourceManagement.res_price[i] * self.ResourceManagement.res_production[i]
            self.ResourceManagement.res_consumption[i] = 0
            self.ResourceManagement.res_production[i] = 0
            
        for i in range(len(self.ResourceManagement.basic_production)):    
            revenue = 0
            for j in range(len(self.ResourceManagement.basic_production[i].production)):
                revenue += self.ResourceManagement.basic_production[i].production[j] * self.ResourceManagement.res_price[j] - self.ResourceManagement.basic_production[i].consumption[j] * self.ResourceManagement.res_price[j]
            if self.ResourceManagement.basic_production[i].quantity > 0:
                self.ResourceManagement.basic_production[i].salary = revenue / (self.ResourceManagement.basic_production[i].workplaces * self.ResourceManagement.basic_production[i].quantity)
            for j in range(len(self.ResourceManagement.basic_production[i].workers)):
                self.ResourceManagement.basic_production[i].workers[j].money += self.ResourceManagement.basic_production[i].salary

        for i in range(len(self.ResourceManagement.advanced_production)):    
            revenue = 0
            for j in range(len(self.ResourceManagement.advanced_production[i].production)):
                revenue += self.ResourceManagement.advanced_production[i].production[j] * self.ResourceManagement.res_price[j] - self.ResourceManagement.advanced_production[i].consumption[j] * self.ResourceManagement.res_price[j]
            if self.ResourceManagement.advanced_production[i].quantity > 0:
                self.ResourceManagement.advanced_production[i].salary = revenue / (self.ResourceManagement.advanced_production[i].workplaces * self.ResourceManagement.advanced_production[i].quantity)
            for j in range(len(self.ResourceManagement.advanced_production[i].workers)):
                self.ResourceManagement.advanced_production[i].workers[j].money += self.ResourceManagement.advanced_production[i].salary

        if self.in_build == True:
            builders_time = 0
            for i in range(len(self.currently_building.res)):
                if self.currently_building.res[i] != 0:
                    work_given = max(0, min(self.currently_building.res[i], self.ResourceManagement.res[i]))
                    self.building_time -= work_given
                    self.ResourceManagement.res[i] -= work_given
                    self.res_done += work_given
            for i in range(len(self.ResourceManagement.advanced_production[6].workers)):
                builders_time += self.ResourceManagement.advanced_production[6].workers[i].workhours + self.ResourceManagement.basic_production[6].workers[i].workhours
            self.building_time -= min(builders_time, self.currently_building.workhours * (self.res_total / self.res_done))
            if self.building_time <= 0:
                self.currently_building.production.quantity += 1
                self.in_build = False
                self.currently_building = None

        for i in range(len(self.ResourceManagement.res)):
            self.budget += self.ResourceManagement.res[i] * self.ResourceManagement.res_price[i]

        for i in range(len(self.ResourceManagement.basic_production)):
            for j in range(len(self.ResourceManagement.basic_production[i].workers)):
                for q in range(len(self.ResourceManagement.basic_production[i].consumption)):
                    self.ResourceManagement.res_consumption[q] += self.ResourceManagement.basic_production[i].consumption[q] * round(self.ResourceManagement.basic_production[i].workers[j].workhours / self.ResourceManagement.basic_production[i].workhours)
                for q in range(len(self.ResourceManagement.basic_production[i].consumption)):
                    self.ResourceManagement.res_production[q] += self.ResourceManagement.basic_production[i].production[q] * round(self.ResourceManagement.basic_production[i].workers[j].workhours / self.ResourceManagement.basic_production[i].workhours)
        
    def control_city(self):
        action = intinput("1: build \n2: assign workers\n3: unassign workers", 1, 3)
        if action == 1:
            build = intinput("1: Basic production spot \n2: Building", 1, 2)
            if build == 1:
                for i in range(len(self.ResourceManagement.basic_production)):
                    print(i+1, ": ", self.ResourceManagement.basic_production[i].name)
                build = intinput("", 1, len(self.ResourceManagement.basic_production)) - 1
                quan = intinput("How many?", 1)
                self.ResourceManagement.basic_production[build].quantity += quan
            elif build == 2:
                if self.in_build == False:
                    for i in range(len(self.ResourceManagement.buildings)):
                        print(i+1, ": ", self.ResourceManagement.buildings[i].name)
                    build = intinput("", 1, len(self.ResourceManagement.buildings))
                    self.in_build = True
                    self.currently_building = self.ResourceManagement.buildings[build]
                    self.res_total = 0
                    self.res_done = 0
                    for i in range(len(self.currently_building.res)):
                        self.res_total += self.currently_building.res[i]
                    self.building_time = self.ResourceManagement.buildings[build].workhours
                    print("building of ", self.ResourceManagement.buildings[build].name, " is in progress")
                else:
                    print("building ", self.ResourceManagement.buildings[build].name, " is already in progress")

        elif action == 2:
            if len(self.unemployed_citizens) != 0:
                print("list of unasigned workers:")
                for i in range(len(self.unemployed_citizens)):
                    print(i + 1, ": ", self.unemployed_citizens[i].fname, self.unemployed_citizens[i].lname)
                choose = intinput("choose worker: ", 1, len(self.unemployed_citizens)) - 1
                adv = intinput("1: basic production \n2: advanced production", 1, 2)
                print("where to?")
                if adv == 1:
                    for i in range(len(self.ResourceManagement.basic_production)):
                        if (self.ResourceManagement.basic_production[i].quantity > 0) & (len(self.ResourceManagement.basic_production[i].workers) < (self.ResourceManagement.basic_production[i].quantity * self.ResourceManagement.basic_production[i].workplaces)):
                            print(i+1,": ", self.ResourceManagement.basic_production[i].name)
                    work = intinput("", 1, len(self.ResourceManagement.basic_production))
                    self.ResourceManagement.basic_production[work-1].workers.append(self.unemployed_citizens[choose])

                elif adv == 2:
                    if len(self.ResourceManagement.advanced_production) > 0:
                        for i in range(len(self.ResourceManagement.advanced_production)):
                            if (self.ResourceManagement.advanced_production[i].quantity > 0) & (len(self.ResourceManagement.advanced_production[i].workers) < (self.ResourceManagement.advanced_production[i].quantity * self.ResourceManagement.advanced_production[i].workplaces)):
                                print(i, ": ", self.ResourceManagement.advanced_production[i].name)
                        work = intinput("", 1, len(self.ResourceManagement.advanced_production))
                        self.ResourceManagement.advanced_production[work-1].workers.append(self.unemployed_citizens[choose])
                    else:
                        print("No advanced production")

                self.unemployed_citizens.pop(choose)

            else:
                print("no unemployed citizens")
        
        elif action == 3:
            print("where from?")
            adv = intinput("1: basic production \n2: advanced production\n", 1, 2)
            if adv == 1:
                for i in range(len(self.ResourceManagement.basic_production)):
                    if len(self.ResourceManagement.basic_production[i].workers) != 0:
                        print(i + 1, ": ", self.ResourceManagement.basic_production[i].name, " \n  workers:", len(self.ResourceManagement.basic_production[i].workers), "\n")
                prod = intinput("", 1, len(self.ResourceManagement.basic_production)) - 1
                for i in range(len(self.ResourceManagement.basic_production[prod].workers)):
                    print(i+1, ": ", self.ResourceManagement.basic_production[prod].workers[i].fname + " " + self.ResourceManagement.basic_production[prod].workers[i].lname)
                worker = intinput("", 1, len(self.ResourceManagement.basic_production[prod].workers)) - 1
                self.unemployed_citizens.append(self.ResourceManagement.basic_production[prod].workers[worker])
                self.ResourceManagement.basic_production[prod].workers.pop(worker)
            elif adv == 2:
                for i in range(len(self.ResourceManagement.advanced_production)):
                    if len(self.ResourceManagement.advanced_production[i].workers) != 0:
                        print(i + 1, ": ", self.ResourceManagement.advanced_production[i].name, " \n  workers:", len(self.ResourceManagement.advanced_production[i].workers), "\n")
                prod = intinput("", 1, len(self.ResourceManagement.advanced_production[i].workers)) - 1
                for i in range(len(self.ResourceManagement.advanced_production[prod].workers)):
                    print(i+1, ": ", self.ResourceManagement.advanced_production[prod].workers[i].fname + " " + self.ResourceManagement.advanced_production[prod].workers[i].lname)
                worker = intinput("", 1, len(self.ResourceManagement.advanced_production[prod].workers)) - 1
                self.unemployed_citizens.append(self.ResourceManagement.advanced_production[prod].workers[worker])
                self.ResourceManagement.advanced_production[prod].workers.pop(worker)

    def economy_information(self):
        for i in range(len(self.ResourceManagement.res)):
            print(self.ResourceManagement.res_names[i])
            print(" in reserve: ", self.ResourceManagement.res[i])
            print(" consumption: ", self.ResourceManagement.res_consumption[i])
            print(" production: ", self.ResourceManagement.res_production[i])
            print(" price: ", round(self.ResourceManagement.res_price[i], 1))

        if self.in_build == True:
            print("currently building: ", self.currently_building.name)
            print("Done: ", (round(((self.currently_building.workhours - self.building_time) / self.currently_building.workhours * 10)) * "|") + ((10 - round(((self.currently_building.workhours - self.building_time)/ self.currently_building.workhours) * 10)) * "-"), " ", round(((self.currently_building.workhours - self.building_time) / self.currently_building.workhours) * 100), "%")
            print("Needs: ")
            for i in range(len(self.currently_building.res)):
                if self.currently_building.res[i] > 0:
                    print(" ", self.currently_building.res[i], " ", self.ResourceManagement.res_names[i])
        print("bbp: ", round(self.bbp, 1))

    def citizen_information(self):
        print("Choose a citizen:")
        print(len(self.citizens))
        for i in range(len(self.citizens)):
            print(i + 1, ": ", self.citizens[i].fname," ", self.citizens[i].lname)
        choose = intinput("")
        print(self.citizens[choose].fname," ", self.citizens[choose].lname)
        print("basic needs:")
        for i in range(len(self.citizens[choose].basic_needs)):
            print(self.ResourceManagement.res_names[i], ": ", self.citizens[choose].basic_needs[i])

        print("second needs:")
        for i in range(len(self.citizens[choose].second_needs)):
            print(self.ResourceManagement.res_names[i], ": ", self.citizens[choose].second_needs[i])
        
    def auto_work(self):
        works = []
        priority = []

        for advanced in self.ResourceManagement.advanced_production:
            if advanced.quantity * advanced.workplaces - len(advanced.workers):
                works.append(advanced)
            else:
                for basic in self.ResourceManagement.basic_production:
                    for i in range(len(basic.production)):
                        if (basic.production[i] > 0) & (advanced.production[i] > 0):
                            works.append(basic)
        
        for i in range(len(works)):
            revenue = 0
            zero_price = 0
            need = 0
            for j in range(len(self.ResourceManagement.res)):
                revenue += (works[i].production[j] - works[i].consumption[j]) * self.ResourceManagement.res_price[j]
                if ((self.ResourceManagement.res_production[j] == 0) & (works[i].production[j] > 0)):
                    zero_price += 1
                if (((self.ResourceManagement.res_production[j] - self.ResourceManagement.res_consumption[j]) < 0) & (works[i].production[j] > 0)):
                    need += works[i].production[j]
            priority.append([works[i], revenue, zero_price, need])
        
        priority.sort(key=lambda x: (x[3], x[2], x[1]))

        priority[-1][0].workers.append(self.unemployed_citizens[0])
        self.unemployed_citizens.pop(0)

    def inter_trade(self, citites_list):
        pass

class player_class:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.money = 0
        self.hunger = 0
        self.thirst = 0

def river_generator(river_map, height, width):
    begin_x = random.randint(0, width)
    begin_y = random.randint(0, height)
    for i in range(max(round(height*width*0.1), 1)):
    # Assign the best work to the last unemployed citizen)):
        directions = []
        river_lenght = random.randint(round((height+width)*0.1), round((height+width)*0.4))
        if (((begin_y - river_lenght) < 0) or (river_map[max(0, begin_y - 1)][begin_x] == 1)) == False:
            directions.append(0)
        if (((begin_x - river_lenght) < 0) or (river_map[begin_y][max(0, begin_x-1)] == 1)) == False:
            directions.append(1)
        if ((begin_y + river_lenght > height) or (river_map[min(height, begin_y + 1)][begin_x] == 1)) == False:
            directions.append(2)
        if ((begin_x + river_lenght > width) or (river_map[begin_y][min(width, begin_x + 1)] == 1)) == False:
            directions.append(3)
            
        if not directions:
            begin_x = random.randint(0, width)
            begin_y = random.randint(0, height)
            continue
        direction = random.choice(directions)
        if direction == 0:
            for j in range(river_lenght):
                river_map[begin_y - j][begin_x] = 1
            begin_y = random.randint(begin_y - river_lenght, begin_y)
        if direction == 1:
            for j in range(river_lenght):
                river_map[begin_y][begin_x - j] = 1
            begin_x = random.randint(begin_x - river_lenght, begin_x)
        if direction == 2:
            for j in range(river_lenght):
                river_map[begin_y + j][begin_x] = 1
            begin_y = random.randint(begin_y, begin_y + river_lenght)
        if direction == 3:
            for j in range(river_lenght):
                river_map[begin_y][begin_x - j] = 1
            begin_x = random.randint(begin_x, river_lenght + begin_x)
    return river_map

def forest_generator(forest_map, river_map, height, width):
    for _ in range(5):
        while True:
            x = random.randint(0, width)
            y = random.randint(0, height)
            min_distance = float('inf')
            for i in range(height+1):
                for j in range(width+1):
                    if river_map[i][j] == 1:
                        distance = abs(i - y) + abs(j - x)
                        if distance < min_distance:
                            min_distance = distance
            if min_distance > 0:
                break
        forest_size = min_distance
        for i in range(max(0, y-forest_size//2), min(height+1, y+forest_size//2+1)):
            for j in range(max(0, x-forest_size//2), min(width+1, x+forest_size//2+1)):
                forest_map[i][j] = 1
    return forest_map

def villages_generator(cities_map, river_map, height, width, cities_names_1, cities_names_2):
    places = []
    for i in range(height):
        for j in range(width):
            if river_map[i][j] == 1:
                if (river_map[max(0, i - 1)][j] == 0) & (i - 1 > 0):
                    places.append((i - 1, j))
                if (river_map[i][max(0, j - 1)] == 0) & (j - 1 > 0):
                    places.append((i, j - 1))
                if (river_map[min(height, i + 1)][j] == 0) & (i + 1 < height):
                    places.append((i + 1, j))
                if (river_map[i][min(width, j + 1)] == 0) & (j + 1 < width):
                    places.append((i, j + 1))
    for i in range(5):
        place = random.choice(places)
        places.remove(place)
        cities_map[place[0]][place[1]] = 1
        new_city = city(str(random.choice(cities_names_1) + random.choice(cities_names_2)), random.randint(3, 10), place[0], place[1], first_names, last_names)
        cities_list.append(new_city)
        
    return cities_map, cities_list
        
def generation(river_map, forest_map, cities_map, height, width):
    river_map = river_generator(river_map, height, width)
    forest_map = forest_generator(forest_map, river_map, height, width)
    cities_map, cities_list = villages_generator(cities_map, river_map, height, width, cities_names_1, cities_names_2)
    return river_map, forest_map, cities_map, cities_list

def trans_print(world_map, river_map, forest_map, cities_map, height, width):
    world_map = [[0 for _ in range(WM_width+1)] for _ in range(WM_height+1)]
    for i in range(height+1):
        for j in range(width+1):
            river = [0, 0, 0, 0]
            if river_map[i][j] == 1:
                if river_map[max(0, i - 1)][j] == 1:
                    river[0] = 1
                if river_map[i][max(0, j - 1)] == 1:
                    river[1] = 1
                if river_map[min(height, i + 1)][j] == 1:
                    river[2] = 1
                if river_map[i][min(width, j + 1)] == 1:
                    river[3] = 1
                    
                if (river[0] == 0):
                    if (river[1] == 0):
                        if (river[2] == 0):
                            world_map[i][j] = '═'
                        else:
                            if (river[3] == 0):
                                world_map[i][j] = '║'
                            else:
                                world_map[i][j] = '╔'
                    else:
                        if (river[2] == 0):
                                world_map[i][j] = '═'
                        else:
                            if (river[3] == 0):
                                world_map[i][j] = '╗'
                            else:
                                world_map[i][j] = '╦'
                else:
                    if (river[1] == 0):
                        if (river[2] == 0):
                            if (river[3] == 0):
                                world_map[i][j] = '║'
                            else:
                                world_map[i][j] = '╚'
                        else:
                            if (river[3] == 0):
                                world_map[i][j] = '║'
                            else:
                                world_map[i][j] = '╠'
                    else:
                        if (river[2] == 0):
                            if (river[3] == 0):
                                world_map[i][j] = '╝'
                            else:
                                world_map[i][j] = '╩'
                        else:
                            if (river[3] == 0):                                
                                world_map[i][j] = '╣'
                            else:
                                world_map[i][j] = '╬'
            if cities_map[i][j] == 1:
                world_map[i][j] = "⌂"
            if forest_map[i][j] == 1:
                world_map[i][j] = "♣"
            if world_map[i][j] == 0:
                world_map[i][j] = " "
    return world_map

river_map, forest_map, cities_map, cities_list = generation(river_map, forest_map, cities_map, WM_height, WM_width, )

trans_print(world_map, river_map, forest_map, cities_map, WM_height, WM_width)

def player_action(player):
    print("1: move")
    print("2: interact with city")
    print("3: get the information about the city")
    action = intinput("", 1, 4)
    if action == 1:
        print("1: up")
        print("2: left")
        print("3: down")
        print("4: right")
        direction = None
        direction = intinput("", 1, 4)
        if direction == 1:
            player.y -= 1
        if direction == 2:
            player.x -= 1
        if direction == 3:
            player.y += 1
        if direction == 4:
            player.x += 1
    elif action == 2:
        if cities_map[player.y][player.x] == 1:
            for i in range(len(cities_list)):
                if (cities_list[i].x == player.x) & (cities_list[i].y == player.y):
                    cities_list[i].control_city()
        else:
            print("no city")
    elif action == 3:
        if cities_map[player.y][player.x] == 1:
            for i in range(len(cities_list)):
                if (cities_list[i].x == player.x) & (cities_list[i].y == player.y):
                    action = intinput("1: economy information\n2: citizens information\n", 1, 2)
                    if action == 1:
                        cities_list[i].economy_information()
                    elif action == 2:
                        cities_list[i].citizen_information()
        else:
            print("no city")
    return player

def print_map(map, height,width):
    for i in range(height+1):
        for j in range(width+1):
            print(map[i][j], end = "")
        print()
    pass

def turn(player, world_map):  
    next_turn = False
    while next_turn != True:
        world_map = trans_print(world_map, river_map, forest_map, cities_map, WM_height, WM_width)
        world_map[player.y][player.x] = "☺"
        print_map(world_map, WM_height, WM_width)
        player = player_action(player)
        nt = input("next turn? y/n")
        if nt == "y":
            next_turn = True
        os.system('cls' if os.name == 'nt' else 'clear')
    end_turn(cities_list)
    pass

def end_turn(cities):
    for i in range(len(cities)):
        cities[i].upd_population()
        cities[i].economics_upd()

def spawn_player(cities_list):
    print("choose city:")
    for i in range(len(cities_list)):
        while len(cities_list[i].unemployed_citizens) > 0:
            cities_list[i].auto_work()
            cities_list[i].economics_upd()
        print(i + 1,": ", cities_list[i].name)
    city = None
    city = cities_list[intinput("", 1, len(cities_list)) - 1]
    player = player_class("player", city.x, city.y)
    return player

def debug():
    input("1: set salary \"1 - basic, 2 - advanced; production number; salary\"\n2: autowork \"\"")

player = spawn_player(cities_list)

while True:
    turn(player, world_map)