#-*- coding: utf-8 -*-



#en el player model ficar un bool is_player, i ho fica en la vista del player, en el form

#fer form herencia en player


#fer cron en els dovahkiin

from odoo import models, fields, api

import random
from datetime import datetime, timedelta

class septim(models.Model):
    _name = 'septim.septim'
    _description = 'septim.septim'
    
    name = fields.Char()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100


class player(models.Model):
    _name = 'res.partner'
    _description = 'player'
    _inherit = 'res.partner'

    #name = fields.Char(readonly = False, required = True, ondelete ="cascade")
    gold = fields.Float(default = 100, readonly = True, help = "L'or que te el jugador per millorar l'equip, dovahkiins, etc.", ondelete ="cascade")
    dovahkiin = fields.One2many("septim.dovahkiin", "player", String = "dovahkiin", readonly = True, ondelete ="cascade")
    elo = fields.Char(readonly = True, required = True, default = 0, ondelete ="cascade")
    image = fields.Image(size_width = 200, max_height = 200, ondelete ="cascade")
    image_petita = fields.Image(related = "image", size_width=100, max_height = 100, ondelete ="cascade")
    is_player = fields.Boolean(default = False)

class dovahkiin(models.Model):
    _name = 'septim.dovahkiin'
    _description = 'dovahkiin'

    name = fields.Char(required = True)
    player = fields.Many2one("res.partner", required = True)
    elo = fields.Char(readonly = True, required = True, default = 0)
    image = fields.Image(size_width=200, max_height = 200)
    
    price = fields.Char(readonly = True, required = True, default = 50)

    state = fields.Integer(required = True, readonly = True, default = 0) #0 = disponible, 1 = lluitant, 2 = viatjant, 3 = ciutat, 4 = mina


    horse = fields.Many2one("septim.horse", String = "horse", readonly = True, compute = "_many2manyHorse")

    def _many2manyHorse(self):
        for b in self:
            b.horse = self.env['septim.horse'].search([('dovahkiin.id','=',b.id)]).id


    # travel = fields.Many2one("septim.travel", String = "travel", readonly = True, compute = "_many2manyTravel")
    # def _many2manyTravel(self):
    #     for b in self:
    #         b.travel = self.env['septim.travel'].search([('dovahkiin.id','=',b.id)]).id

    place = fields.Many2one("septim.place", String = "place", readonly = True, compute = "_many2manyPlace")
    def _many2manyPlace(self):
        for b in self:
            b.place = self.env['septim.place'].search([('dovahkiin.id','=',b.id)]).id 

    force = fields.Float(default = 10, readonly = True)
    health = fields.Float(default = 50, readonly = True)
    maxhealth = fields.Float(default = 50, readonly = True)
    armor = fields.Float(default = 10, readonly = True)
    critical_chance = fields.Float(default = 10, readonly = True)
    critical_damage = fields.Float(default = 10, readonly = True)
    poison_chance = fields.Float(default = 0, readonly = True)
    poison_damage = fields.Float(default = 0, readonly = True)


    force_helmet = fields.Float(default = 0, readonly = True)
    maxhealth_helmet = fields.Float(default = 0, readonly = True)
    armor_helmet = fields.Float(default = 0, readonly = True)
    critical_chance_helmet = fields.Float(default = 0, readonly = True)
    critical_damage_helmet = fields.Float(default = 0, readonly = True)
    poison_chance_helmet = fields.Float(default = 0, readonly = True)
    poison_damage_helmet = fields.Float(default = 0, readonly = True)

    force_chestplate = fields.Float(default = 0, readonly = True)
    maxhealth_chestplate = fields.Float(default = 0, readonly = True)
    armor_chestplate = fields.Float(default = 0, readonly = True)
    critical_chance_chestplate = fields.Float(default = 0, readonly = True)
    critical_damage_chestplate = fields.Float(default = 0, readonly = True)
    poison_chance_chestplate = fields.Float(default = 0, readonly = True)
    poison_damage_chestplate = fields.Float(default = 0, readonly = True)

    force_leggins = fields.Float(default = 0, readonly = True)
    maxhealth_leggins = fields.Float(default = 0, readonly = True)
    armor_leggins = fields.Float(default = 0, readonly = True)
    critical_chance_leggins = fields.Float(default = 0, readonly = True)
    critical_damage_leggins = fields.Float(default = 0, readonly = True)
    poison_chance_leggins = fields.Float(default = 0, readonly = True)
    poison_damage_leggins = fields.Float(default = 0, readonly = True)

    force_boots = fields.Float(default = 0, readonly = True)
    maxhealth_boots = fields.Float(default = 0, readonly = True)
    armor_boots = fields.Float(default = 0, readonly = True)
    critical_chance_boots = fields.Float(default = 0, readonly = True)
    critical_damage_boots = fields.Float(default = 0, readonly = True)
    poison_chance_boots = fields.Float(default = 0, readonly = True)
    poison_damage_boots = fields.Float(default = 0, readonly = True)

    force_weapon = fields.Float(default = 0, readonly = True)
    critical_chance_weapon = fields.Float(default = 0, readonly = True)
    critical_damage_weapon = fields.Float(default = 0, readonly = True)
    poison_chance_weapon = fields.Float(default = 0, readonly = True)
    poison_damage_weapon = fields.Float(default = 0, readonly = True)

    force_total = fields.Float(compute = "_total_force", readonly = True)
    maxhealth_total = fields.Float(compute = "_total_maxhealth", readonly = True)
    armor_total = fields.Float(compute = "_total_armor", readonly = True)
    critical_chance_total = fields.Float(compute = "_total_critical_chance", readonly = True)
    critical_damage_total = fields.Float(compute = "_total_critical_damage", readonly = True)
    poison_chance_total = fields.Float(compute = "_total_poison_chance", readonly = True)
    poison_damage_total = fields.Float(compute = "_total_poison_damage", readonly = True)

    #recursos
    food = fields.Float(default = 100, readonly = True)
    sleep = fields.Float(default = 100, readonly = True)


  @api.model
    def produce(self):  # ORM CRON
        self.search([]).produce_gold()


    def produce_gold(self):
            for docahkiin in self:
                water = player.gold + colony.water_production
                metal = colony.metal + colony.metal_production
                hydrogen = colony.hydrogen + colony.hydrogen_production
                food = colony.food + colony.food_production
                energy = colony.energy_production

                colony.write({
                    "water": water,
                    "metal": metal,
                    "hydrogen": hydrogen,
                    "food": food,
                    "energy": energy
                })



    @api.model
    def create(self, values):
        new_id = super(dovahkiin, self).create(values)
        new_id.player.gold = new_id.player.gold - 50;
        return new_id

    def _total_force(self):
        for dovahkiin in self:
            dovahkiin.force_total = dovahkiin.force + dovahkiin.force_helmet + dovahkiin.force_chestplate + dovahkiin.force_leggins + dovahkiin.force_boots + dovahkiin.force_weapon;

    def _total_maxhealth(self):
        for dovahkiin in self:
            dovahkiin.maxhealth_total = dovahkiin.maxhealth + dovahkiin.maxhealth_helmet + dovahkiin.maxhealth_chestplate + dovahkiin.maxhealth_leggins + dovahkiin.maxhealth_boots;

    def _total_armor(self):
        for dovahkiin in self:
            dovahkiin.armor_total = dovahkiin.armor + dovahkiin.armor_helmet + dovahkiin.armor_chestplate + dovahkiin.armor_leggins + dovahkiin.armor_boots;
            
    def _total_critical_chance(self):
        for dovahkiin in self:
            dovahkiin.critical_chance_total = dovahkiin.critical_chance + dovahkiin.critical_chance_helmet + dovahkiin.critical_chance_chestplate + dovahkiin.critical_chance_leggins + dovahkiin.critical_chance_boots + dovahkiin.critical_chance_weapon;

    def _total_critical_damage(self):
        for dovahkiin in self:
            dovahkiin.critical_damage_total = dovahkiin.critical_damage + dovahkiin.critical_damage_helmet + dovahkiin.critical_damage_chestplate + dovahkiin.critical_damage_leggins + dovahkiin.critical_damage_boots + dovahkiin.critical_damage_weapon;

    def _total_critical_damage(self):
        for dovahkiin in self:
            dovahkiin.critical_damage_total = dovahkiin.critical_damage + dovahkiin.critical_damage_helmet + dovahkiin.critical_damage_chestplate + dovahkiin.critical_damage_leggins + dovahkiin.critical_damage_boots + dovahkiin.critical_damage_weapon;

    def _total_poison_chance(self):
        for dovahkiin in self:
            dovahkiin.poison_chance_total = dovahkiin.poison_chance + dovahkiin.poison_chance_helmet + dovahkiin.poison_chance_chestplate + dovahkiin.poison_chance_leggins + dovahkiin.poison_chance_boots + dovahkiin.poison_chance_weapon;

    def _total_poison_damage(self):
        for dovahkiin in self:
            dovahkiin.poison_damage_total = dovahkiin.poison_damage + dovahkiin.poison_damage_helmet + dovahkiin.poison_damage_chestplate + dovahkiin.poison_damage_leggins + dovahkiin.poison_damage_boots + dovahkiin.poison_damage_weapon;


class battle(models.Model):
    _name = 'septim.battle'
    _description = 'battle'

    player1 = fields.Many2one("res.partner", required = True)
    dovahkiin_player1 = fields.Many2one("septim.dovahkiin", required = True)
    player2 = fields.Many2one("res.partner", required = True)
    dovahkiin_player2 = fields.Many2one("septim.dovahkiin", required = True)

    winner = fields.Many2one("res.partner", compute = "_simulate_battle", readonly = True)
    loser = fields.Many2one("res.partner", compute = "_simulate_battle", readonly = True)

    start_date = fields.Datetime(required = True, default = fields.Datetime.now, readonly=True)
    end_date = fields.Datetime(compute = "_end_date_battle", readonly = True)
    progress = fields.Float(compute="_compute_progress", readonly = True)

    state = fields.Selection([('1', 'Preparation'), ('2', 'Launched'), ('3', 'Finished')], default='1')

    @api.onchange('player1')
    def _filter_player2(self):                                             
      return { 'domain': {'player2': [('id','!=',self.player1.id)]} }  

    @api.onchange('player2')
    def _filter_player1(self):                                             
      return { 'domain': {'player1': [('id','!=',self.player2.id)]} }  

    @api.onchange('player1')
    def _filter_dovahkiin_player1(self):                                             
        return { 'domain': {'dovahkiin_player1': [('player.id','=',self.player1.id)]} } # fer un and de l'state (si està picant no pot lluitar, osi està en altra lluita )
    
    @api.onchange('player2')
    def _filter_dovahkiin_player2(self):                                             
        return { 'domain': {'dovahkiin_player2': [('player.id','=',self.player2.id)]} }  

    def _end_date_battle(self):
        for battle in self:
            data = fields.Datetime.from_string(battle.start_date)
            data = data+timedelta(hours=1)
            battle.end_date = fields.Datetime.to_string(data)

    def _compute_progress(self):
        for rec in self:
            rec.progress = 0

            if rec.start_date and rec.end_date:
                total_seconds = rec.end_date - rec.start_date

                if fields.Datetime.now() >  rec.end_date:
                    rec.progress = 100
                else:
                    progress = rec.end_date - fields.Datetime.now()
                    try:
                        percentage = ((total_seconds.seconds*60) - (progress.seconds*60)) * 100 / (total_seconds.seconds*60)
                        rec.progress = percentage
                    except ZeroDivisionError:
                        rec.progress = 0

    @api.model
    def create(self, values):
        new_id = super(battle, self).create(values)
        new_id.state = "2";
        return new_id


    def _simulate_battle():
        for s in self:

            tornsPlayer1 = 0;
            tornsPlayer2 = 0;

            #atac jugador1
            while(dovahkiin_player2.health > 0):
                tornsPlayer1 = tornsPlayer1 + 1;

                dovahkiin_player2.health = dovahkiin_player2.health - (dovahkiin_player1.force_total - dovahkiin_player2.armor_total) 

                critProb = random.randint(0, 100);
                if(critProb > 0 and critProb < dovahkiin_player1.critical_chance_total):
                    dovahkiin_player2.health = dovahkiin_player2.health - (dovahkiin_player1.critical_damage_total - dovahkiin_player2.armor_total);  

                poisonProb = random.randint(0, 100);
                if(poisonProb > 0 and poisonProb < dovahkiin_player1.poison_chance_total):
                    dovahkiin_player2.health = dovahkiin_player2.health - dovahkiin_player1.poison_damage_total;  

            #atac jugador2
            while(dovahkiin_player1.health > 0):
                tornsPlayer2 = tornsPlayer2 + 1;

                dovahkiin_player1.health = dovahkiin_player1.health - (dovahkiin_player2.force_total - dovahkiin_player1.armor_total) 

                critProb = random.randint(0, 100);
                if(critProb > 0 and critProb < dovahkiin_player2.critical_chance_total):
                    dovahkiin_player1.health = dovahkiin_player1.health - (dovahkiin_player2.critical_damage_total - dovahkiin_player1.armor_total);  

                poisonProb = random.randint(0, 100);
                if(poisonProb > 0 and poisonProb < dovahkiin_player2.poison_chance_total):
                    dovahkiin_player1.health = dovahkiin_player1.health - dovahkiin_player1.poison_damage_total;  


            if tornsPlayer2 > tornsPlayer1:
                s.winner = s.player1
                s.loser = s.player2

            if tornsPlayer1 > tornsPlayer2:
                s.winner = s.player2
                s.loser = s.player1

            if tornsPlayer1 == tornsPlayer2:
                s.winner = False
                s.loser = False       
        

class place(models.Model):
    _name = 'septim.place'
    _description = 'place'

    typex = fields.Integer(default = 0, readonly = False) #1 = ciutat, #2 = mina/cada X temps dóna or(?, #
    sleepx = fields.Float(default = 0, readonly = True)
    goldx = fields.Float(default = 0, readonly = True)
    foodx = fields.Float(default = 0, readonly = True)
    dovahkiin = fields.Many2one("septim.dovahkiin", required = True)

    # travel = fields.Many2one("septim.travel", required = False)
    # def _many2manyPlace(self):
    #     for b in self:
    #         b.place = self.env['septim.place'].search([('dovahkiin.id','=',b.id)]).id 

    @api.model
    def create(self, values):
        new_id = super(place, self).create(values)
        if(new_id.typex == 0):
            new_id.sleepx = random.randint(1, 10);
            new_id.foodx = random.randint(1, 10);
            new_id.goldx = 0;
        
        if(new_id.typex == 1):
            new_id.sleepx = random.randint(-10, -1);
            new_id.foodx = -5;
            new_id.goldx = random.randint(1, 10);
        
        return new_id


    #ho has acabat de crear la ciutats, ni tens clar com fer-ho


class horse(models.Model):
    _name = 'septim.horse'
    _description = 'horse'

    name = fields.Char(readonly = False, required = True)
    uses = fields.Integer(default = 5, readonly = True)
    level = fields.Integer(default = 1, readonly = True)
    price = fields.Integer(default = 0, readonly = True)
    dovahkiin = fields.Many2one("septim.dovahkiin", required = True)

    @api.model
    def create(self, values):
        new_id = super(horse, self).create(values)
        new_id.dovahkiin.player.gold = new_id.dovahkiin.player.gold - 20;
        return new_id


class forge(models.Model):
    _name = 'septim.forge'
    _description = 'forge'

    player = fields.Many2one("res.partner", required = True)
    dovahkiin = fields.Many2one("septim.dovahkiin", required = True)

    force = fields.Float(compute = "_default_force_forge", readonly = True) 
    health = fields.Float(compute = "_default_health_forge", readonly = True)
    maxhealth = fields.Float(compute = "_default_maxhealth_forge", readonly = True)
    armor = fields.Float(compute = "_default_armor_forge", readonly = True)
    critical_chance = fields.Float(compute = "_default_critical_chance_forge", readonly = True)
    critical_damage = fields.Float(compute = "_default_critical_damage_forge", readonly = True)
    poison_chance = fields.Float(compute = "_default_poison_chance_forge", readonly = True)
    poison_damage = fields.Float(compute = "_default_poison_damage_forge", readonly = True)

    force_helmet = fields.Float(compute = "_default_force_helmet_forge", readonly = True)
    maxhealth_helmet = fields.Float(compute = "_default_maxhealth_helmet_forge", readonly = True)
    armor_helmet = fields.Float(compute = "_default_armor_helmet_forge", readonly = True)
    critical_chance_helmet = fields.Float(compute = "_default_critical_chance_helmet_forge", readonly = True)
    critical_damage_helmet = fields.Float(compute = "_default_critical_damage_helmet_forge", readonly = True)
    poison_chance_helmet = fields.Float(compute = "_default_poison_chance_helmet_forge", readonly = True)
    poison_damage_helmet = fields.Float(compute = "_default_poison_damage_helmet_forge", readonly = True)

    force_chestplate = fields.Float(compute = "_default_force_chestplate_forge", readonly = True)
    maxhealth_chestplate = fields.Float(compute = "_default_maxhealth_chestplate_forge", readonly = True)
    armor_chestplate = fields.Float(compute = "_default_armor_chestplate_forge", readonly = True)
    critical_chance_chestplate = fields.Float(compute = "_default_critical_chance_chestplate_forge", readonly = True)
    critical_damage_chestplate = fields.Float(compute = "_default_critical_damage_chestplate_forge", readonly = True)
    poison_chance_chestplate = fields.Float(compute = "_default_poison_chance_chestplate_forge", readonly = True)
    poison_damage_chestplate = fields.Float(compute = "_default_poison_damage_chestplate_forge", readonly = True)

    force_leggins = fields.Float(compute = "_default_force_leggins_forge", readonly = True)
    maxhealth_leggins = fields.Float(compute = "_default_maxhealth_leggins_forge", readonly = True)
    armor_leggins = fields.Float(compute = "_default_armor_leggins_forge", readonly = True)
    critical_chance_leggins = fields.Float(compute = "_default_critical_chance_leggins_forge", readonly = True)
    critical_damage_leggins = fields.Float(compute = "_default_critical_damage_leggins_forge", readonly = True)
    poison_chance_leggins = fields.Float(compute = "_default_poison_chance_leggins_forge", readonly = True)
    poison_damage_leggins = fields.Float(compute = "_default_poison_damage_leggins_forge", readonly = True)

    force_boots = fields.Float(compute = "_default_force_boots_forge", readonly = True)
    maxhealth_boots = fields.Float(compute = "_default_maxhealth_boots_forge", readonly = True)
    armor_boots = fields.Float(compute = "_default_armor_boots_forge", readonly = True)
    critical_chance_boots = fields.Float(compute = "_default_critical_chance_boots_forge", readonly = True)
    critical_damage_boots = fields.Float(compute = "_default_critical_damage_boots_forge", readonly = True)
    poison_chance_boots = fields.Float(compute = "_default_poison_chance_boots_forge", readonly = True)
    poison_damage_boots = fields.Float(compute = "_default_poison_damage_boots_forge", readonly = True)

    force_weapon = fields.Float(compute = "_default_force_weapon_forge", readonly = True)
    critical_chance_weapon = fields.Float(compute = "_default_critical_chance_weapon_forge", readonly = True)
    critical_damage_weapon = fields.Float(compute = "_default_critical_damage_weapon_forge", readonly = True)
    poison_chance_weapon = fields.Float(compute = "_default_poison_chance_weapon_forge", readonly = True)
    poison_damage_weapon = fields.Float(compute = "_default_poison_damage_weapon_forge", readonly = True)

    force_total = fields.Float(compute = "_default_force_total_forge", readonly = True)
    maxhealth_total = fields.Float(compute = "_default_maxhealth_total_forge", readonly = True)
    armor_total = fields.Float(compute = "_default_armor_total_forge", readonly = True)
    critical_chance_total = fields.Float(compute = "_default_critical_chance_total_forge", readonly = True)
    critical_damage_total = fields.Float(compute = "_default_critical_damage_total_forge", readonly = True)
    poison_chance_total = fields.Float(compute = "_default_poison_chance_total_forge", readonly = True)
    poison_damage_total = fields.Float(compute = "_default_poison_damage_total_forge", readonly = True)

    @api.onchange('player')
    def _filter_dovahkiin_player(self):                                             
        return { 'domain': {'dovahkiin': [('player.id','=',self.player.id)]} }

    @api.onchange('dovahkiin')
    def _stats_dova(self): 

        self.force = self.dovahkiin.force;
        self.health = self.dovahkiin.health;
        self.maxhealth = self.dovahkiin.maxhealth;
        self.armor = self.dovahkiin.armor;
        self.critical_chance = self.dovahkiin.critical_chance;
        self.critical_damage = self.dovahkiin.critical_damage;
        self.poison_chance = self.dovahkiin.poison_chance;
        self.poison_damage = self.dovahkiin.poison_damage;

        self.force_helmet = self.dovahkiin.force_helmet;
        self.maxhealth_helmet = self.dovahkiin.maxhealth_helmet;
        self.armor_helmet = self.dovahkiin.armor_helmet;
        self.critical_chance_helmet = self.dovahkiin.critical_chance_helmet;
        self.critical_damage_helmet = self.dovahkiin.critical_damage_helmet;
        self.poison_chance_helmet = self.dovahkiin.poison_chance_helmet;
        self.poison_damage_helmet = self.dovahkiin.poison_damage_helmet;

        self.force_chestplate = self.dovahkiin.force_chestplate;
        self.maxhealth_chestplate = self.dovahkiin.maxhealth_chestplate;
        self.armor_chestplate = self.dovahkiin.armor_chestplate;
        self.critical_chance_chestplate = self.dovahkiin.critical_chance_chestplate;
        self.critical_damage_chestplate = self.dovahkiin.critical_damage_chestplate;
        self.poison_chance_chestplate = self.dovahkiin.poison_chance_chestplate;
        self.poison_damage_chestplate = self.dovahkiin.poison_damage_chestplate;

        self.force_leggins = self.dovahkiin.force_leggins;
        self.maxhealth_leggins = self.dovahkiin.maxhealth_leggins;
        self.armor_leggins = self.dovahkiin.armor_leggins;
        self.critical_chance_leggins = self.dovahkiin.critical_chance_leggins;
        self.critical_damage_leggins = self.dovahkiin.critical_damage_leggins;
        self.poison_chance_leggins = self.dovahkiin.poison_chance_leggins;
        self.poison_damage_leggins = self.dovahkiin.poison_damage_leggins;

        self.force_boots = self.dovahkiin.force_boots;
        self.maxhealth_boots = self.dovahkiin.maxhealth_boots;
        self.armor_boots = self.dovahkiin.armor_boots;
        self.critical_chance_boots = self.dovahkiin.critical_chance_boots;
        self.critical_damage_boots = self.dovahkiin.critical_damage_boots;
        self.poison_chance_boots = self.dovahkiin.poison_chance_boots;
        self.poison_damage_boots = self.dovahkiin.poison_damage_boots;

        self.critical_chance_weapon = self.dovahkiin.critical_chance_weapon;
        self.critical_damage_weapon = self.dovahkiin.critical_damage_weapon;
        self.poison_chance_weapon = self.dovahkiin.poison_chance_weapon;
        self.poison_damage_weapon = self.dovahkiin.poison_damage_weapon;

        self.force_total = self.dovahkiin.force_total;
        self.maxhealth_total = self.dovahkiin.maxhealth_total;
        self.armor_total = self.dovahkiin.armor_total;
        self.critical_chance_total = self.dovahkiin.critical_chance_total;
        self.critical_damage_total = self.dovahkiin.critical_damage_total;
        self.poison_chance_total = self.dovahkiin.poison_chance_total;
        self.poison_damage_total = self.dovahkiin.poison_damage_total;
        
    
        return { 'domain': {'dovahkiin': [('player.id','=',self.player.id)]} }

    def update_total(self):

        self.force_total = self.dovahkiin.force_total;
        self.maxhealth_total = self.dovahkiin.maxhealth_total;
        self.armor_total = self.dovahkiin.armor_total;
        self.critical_chance_total = self.dovahkiin.critical_chance_total;
        self.critical_damage_total = self.dovahkiin.critical_damage_total;
        self.poison_chance_total = self.dovahkiin.poison_chance_total;
        self.poison_damage_total = self.dovahkiin.poison_damage_total;

    def generate_helmet(self):

            if(self.player.gold >= 5):
                self.player.gold =  self.player.gold - 5

                force = random.randint(0, 20);
                maxhealth = random.randint(0, 20);
                armor = random.randint(0, 20);
                critical_chance = random.randint(0, 20);
                critical_damage = random.randint(0, 20);
                poison_chance = random.randint(0, 20);
                poison_damage = random.randint(0, 20);

                self.force_helmet = force;
                self.maxhealth_helmet = maxhealth;
                self.armor_helmet = armor;
                self.critical_chance_helmet = critical_chance;
                self.critical_damage_helmet = critical_damage;
                self.poison_chance_helmet = poison_chance
                self.poison_damage_helmet = poison_damage;

                self.dovahkiin.force_helmet = force;
                self.dovahkiin.maxhealth_helmet = maxhealth;
                self.dovahkiin.armor_helmet = armor;
                self.dovahkiin.critical_chance_helmet = critical_chance
                self.dovahkiin.critical_damage_helmet = critical_damage;
                self.dovahkiin.poison_chance_helmet = poison_chance;
                self.dovahkiin.poison_damage_helmet = poison_damage;
            
    def generate_chestplate(self):

            if(self.player.gold >= 5):
                self.player.gold =  self.player.gold - 5

                force = random.randint(0, 20);
                maxhealth = random.randint(0, 20);
                armor = random.randint(0, 20);
                critical_chance = random.randint(0, 20);
                critical_damage = random.randint(0, 20);
                poison_chance = random.randint(0, 20);
                poison_damage = random.randint(0, 20);

                self.force_chestplate = force;
                self.maxhealth_chestplate = maxhealth;
                self.armor_chestplate = armor;
                self.critical_chance_chestplate = critical_chance;
                self.critical_damage_chestplate = critical_damage;
                self.poison_chance_chestplate = poison_chance
                self.poison_damage_chestplate = poison_damage;

                self.dovahkiin.force_chestplate = force;
                self.dovahkiin.maxhealth_chestplate = maxhealth;
                self.dovahkiin.armor_chestplate = armor;
                self.dovahkiin.critical_chance_chestplate = critical_chance
                self.dovahkiin.critical_damage_chestplate = critical_damage;
                self.dovahkiin.poison_chance_chestplate = poison_chance;
                self.dovahkiin.poison_damage_chestplate = poison_damage;

    def generate_leggins(self):

            if(self.player.gold >= 5):
                self.player.gold =  self.player.gold - 5

                force = random.randint(0, 20);
                maxhealth = random.randint(0, 20);
                armor = random.randint(0, 20);
                critical_chance = random.randint(0, 20);
                critical_damage = random.randint(0, 20);
                poison_chance = random.randint(0, 20);
                poison_damage = random.randint(0, 20);

                self.force_leggins = force;
                self.maxhealth_leggins = maxhealth;
                self.armor_leggins = armor;
                self.critical_chance_leggins = critical_chance;
                self.critical_damage_leggins = critical_damage;
                self.poison_chance_leggins = poison_chance
                self.poison_damage_leggins = poison_damage;

                self.dovahkiin.force_leggins = force;
                self.dovahkiin.maxhealth_leggins = maxhealth;
                self.dovahkiin.armor_leggins = armor;
                self.dovahkiin.critical_chance_leggins = critical_chance
                self.dovahkiin.critical_damage_leggins = critical_damage;
                self.dovahkiin.poison_chance_leggins = poison_chance;
                self.dovahkiin.poison_damage_leggins = poison_damage;

    def generate_boots(self):

            if(self.player.gold >= 5):
                self.player.gold =  self.player.gold - 5

                force = random.randint(0, 20);
                maxhealth = random.randint(0, 20);
                armor = random.randint(0, 20);
                critical_chance = random.randint(0, 20);
                critical_damage = random.randint(0, 20);
                poison_chance = random.randint(0, 20);
                poison_damage = random.randint(0, 20);

                self.force_boots = force;
                self.maxhealth_boots = maxhealth;
                self.armor_boots = armor;
                self.critical_chance_boots = critical_chance;
                self.critical_damage_boots = critical_damage;
                self.poison_chance_boots = poison_chance
                self.poison_damage_boots = poison_damage;

                self.dovahkiin.force_boots = force;
                self.dovahkiin.maxhealth_boots = maxhealth;
                self.dovahkiin.armor_boots = armor;
                self.dovahkiin.critical_chance_boots = critical_chance
                self.dovahkiin.critical_damage_boots = critical_damage;
                self.dovahkiin.poison_chance_boots = poison_chance;
                self.dovahkiin.poison_damage_boots = poison_damage;

    def generate_weapon(self):

            if(self.player.gold >= 5):
                self.player.gold =  self.player.gold - 5

                force = random.randint(0, 20);
                critical_chance = random.randint(0, 20);
                critical_damage = random.randint(0, 20);
                poison_chance = random.randint(0, 20);
                poison_damage = random.randint(0, 20);

                self.force_weapon = force;
                self.critical_chance_weapon = critical_chance;
                self.critical_damage_weapon = critical_damage;
                self.poison_chance_weapon = poison_chance
                self.poison_damage_weapon = poison_damage;
                self.dovahkiin.force_weapon = force;
                self.dovahkiin.critical_chance_weapon = critical_chance
                self.dovahkiin.critical_damage_weapon = critical_damage;
                self.dovahkiin.poison_chance_weapon = poison_chance;
                self.dovahkiin.poison_damage_weapon = poison_damage;

    def _default_force_forge(self):
        for f in self:
            f.force = f.dovahkiin.force;

    def _default_health_forge(self):
        for f in self:
            f.health = f.dovahkiin.health;

    def _default_maxhealth_forge(self):
        for f in self:
            f.maxhealth = f.dovahkiin.maxhealth;

    def _default_armor_forge(self):
        for f in self:
            f.armor = f.dovahkiin.armor;

    def _default_critical_chance_forge(self):
        for f in self:
            f.critical_chance = f.dovahkiin.critical_chance;

    def _default_critical_damage_forge(self):
        for f in self:
            f.critical_damage = f.dovahkiin.critical_damage;

    def _default_poison_chance_forge(self):
        for f in self:
            f.poison_chance = f.dovahkiin.poison_chance;
            
    def _default_poison_damage_forge(self):
        for f in self:
            f.poison_damage = f.dovahkiin.poison_damage;

    def _default_force_helmet_forge(self):
        for f in self:
            f.force_helmet = f.dovahkiin.force_helmet;

    def _default_maxhealth_helmet_forge(self):
        for f in self:
            f.maxhealth_helmet = f.dovahkiin.maxhealth_helmet;

    def _default_armor_helmet_forge(self):
        for f in self:
            f.armor_helmet = f.dovahkiin.armor_helmet;

    def _default_critical_chance_helmet_forge(self):
        for f in self:
            f.critical_chance_helmet = f.dovahkiin.critical_chance_helmet;

    def _default_critical_damage_helmet_forge(self):
        for f in self:
            f.critical_damage_helmet = f.dovahkiin.critical_damage_helmet;

    def _default_poison_chance_helmet_forge(self):
        for f in self:
            f.poison_chance_helmet = f.dovahkiin.poison_chance_helmet;
            
    def _default_poison_damage_helmet_forge(self):
        for f in self:
            f.poison_damage_helmet = f.dovahkiin.poison_damage_helmet;

    def _default_force_chestplate_forge(self):
        for f in self:
            f.force_chestplate = f.dovahkiin.force_chestplate;

    def _default_maxhealth_chestplate_forge(self):
        for f in self:
            f.maxhealth_chestplate = f.dovahkiin.maxhealth_chestplate;

    def _default_armor_chestplate_forge(self):
        for f in self:
            f.armor_chestplate = f.dovahkiin.armor_chestplate;

    def _default_critical_chance_chestplate_forge(self):
        for f in self:
            f.critical_chance_chestplate = f.dovahkiin.critical_chance_chestplate;

    def _default_critical_damage_chestplate_forge(self):
        for f in self:
            f.critical_damage_chestplate = f.dovahkiin.critical_damage_chestplate;

    def _default_poison_chance_chestplate_forge(self):
        for f in self:
            f.poison_chance_chestplate = f.dovahkiin.poison_chance_chestplate;
            
    def _default_poison_damage_chestplate_forge(self):
        for f in self:
            f.poison_damage_chestplate = f.dovahkiin.poison_damage_chestplate;

    def _default_force_leggins_forge(self):
        for f in self:
            f.force_leggins = f.dovahkiin.force_leggins;

    def _default_maxhealth_leggins_forge(self):
        for f in self:
            f.maxhealth_leggins = f.dovahkiin.maxhealth_leggins;

    def _default_armor_leggins_forge(self):
        for f in self:
            f.armor_leggins = f.dovahkiin.armor_leggins;

    def _default_critical_chance_leggins_forge(self):
        for f in self:
            f.critical_chance_leggins = f.dovahkiin.critical_chance_leggins;

    def _default_critical_damage_leggins_forge(self):
        for f in self:
            f.critical_damage_leggins = f.dovahkiin.critical_damage_leggins;

    def _default_poison_chance_leggins_forge(self):
        for f in self:
            f.poison_chance_leggins = f.dovahkiin.poison_chance_leggins;
            
    def _default_poison_damage_leggins_forge(self):
        for f in self:
            f.poison_damage_leggins = f.dovahkiin.poison_damage_leggins;

    def _default_force_boots_forge(self):
        for f in self:
            f.force_boots = f.dovahkiin.force_boots;

    def _default_maxhealth_boots_forge(self):
        for f in self:
            f.maxhealth_boots = f.dovahkiin.maxhealth_boots;

    def _default_armor_boots_forge(self):
        for f in self:
            f.armor_boots = f.dovahkiin.armor_boots;

    def _default_critical_chance_boots_forge(self):
        for f in self:
            f.critical_chance_boots = f.dovahkiin.critical_chance_boots;

    def _default_critical_damage_boots_forge(self):
        for f in self:
            f.critical_damage_boots = f.dovahkiin.critical_damage_boots;

    def _default_poison_chance_boots_forge(self):
        for f in self:
            f.poison_chance_boots = f.dovahkiin.poison_chance_boots;
            
    def _default_poison_damage_boots_forge(self):
        for f in self:
            f.poison_damage_boots = f.dovahkiin.poison_damage_boots;

    def _default_force_weapon_forge(self):
        for f in self:
            f.force_weapon = f.dovahkiin.force_weapon;

    def _default_critical_chance_weapon_forge(self):
        for f in self:
            f.critical_chance_weapon = f.dovahkiin.critical_chance_weapon;

    def _default_critical_damage_weapon_forge(self):
        for f in self:
            f.critical_damage_weapon = f.dovahkiin.critical_damage_weapon;

    def _default_poison_chance_weapon_forge(self):
        for f in self:
            f.poison_chance_weapon = f.dovahkiin.poison_chance_weapon;
            
    def _default_poison_damage_weapon_forge(self):
        for f in self:
            f.poison_damage_weapon = f.dovahkiin.poison_damage_weapon;

    def _default_force_total_forge(self):
        for f in self:
            f.force_total = f.dovahkiin.force_total;

    def _default_maxhealth_total_forge(self):
        for f in self:
            f.maxhealth_total = f.dovahkiin.maxhealth_total;

    def _default_armor_total_forge(self):
        for f in self:
            f.armor_total = f.dovahkiin.armor_total;

    def _default_critical_chance_total_forge(self):
        for f in self:
            f.critical_chance_total = f.dovahkiin.critical_chance_total;

    def _default_critical_damage_total_forge(self):
        for f in self:
            f.critical_damage_total = f.dovahkiin.critical_damage_total;

    def _default_poison_chance_total_forge(self):
        for f in self:
            f.poison_chance_total = f.dovahkiin.poison_chance_total;
            
    def _default_poison_damage_total_forge(self):
        for f in self:
            f.poison_damage_total = f.dovahkiin.poison_damage_total;


# class travel(models.Model):
#     _name = 'septim.travel'
#     _description = 'travel'

#     horesx = fields.Float(default = 8, readonly = True)
#     horesFinals = fields.Float(default = 0, readonly = True);
#     destiny = fields.Integer(default = 0, readonly = False, required = True)

#     dovahkiin = fields.Many2one("septim.dovahkiin", required = True, readonly = False)

#     place = fields.Many2one("septim.place")

#     @api.model
#     def create(self, values):
#         new_id = super(travel, self).create(values)
#         #falla algo per ací, moltíssima sort
#         new_id.place = self.env["septim.place"].create({"type" : new_id.destiny, "dovahkiin" : new_id.dovahkiin})

#         return new_id


################# WIZARDS #################

class player_wizard(models.TransientModel):
    _name = 'septim.player_wizard'
    _description = 'Wizzard create player'
    
    def _default_client(self):
        return self.env['res.partner'].browse(self._context.get('active_id')) 

    name = fields.Many2one('res.partner',default=_default_client, required=True)
    gold = fields.Float(default = 100, readonly = True, help = "L'or que te el jugador per millorar l'equip, dovahkiins, etc.", ondelete ="cascade")
    dovahkiin = fields.One2many("septim.dovahkiin", "player", String = "dovahkiin", readonly = True, ondelete ="cascade")
    elo = fields.Char(readonly = True, required = True, default = 0, ondelete ="cascade")
    image = fields.Image(size_width = 200, max_height = 200, ondelete ="cascade")
    

    @api.model
    def default_get(self, default_fields):
        result = super(player_wizard, self).default_get(default_fields)
        return result

    def create_player(self):
        self.ensure_one()
        self.name.write({'gold': self.gold,
                         'elo': self.elo,
                         'image': self.image,
                         'is_player': True
                         })
