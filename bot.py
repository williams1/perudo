class WilliamsPerudoBot:

	def __init__(number_players: int, dice_per_player: int):
		self.num_players = number_players
		self.num_dice = [dice_per_player]*number_players
		self.my_dice = []
		self.my_dice_number = dice_per_player
		self.first_bids = [None]*number_players
		self.first_player = None
		self.one_die_round = False


	def action(self, action_type: str, **kwargs):
		match action_type:
			case "bid":
				die_face = kwargs.die #int
				number_of_dice = kwargs.number #int
				pass #integrate into function

			case "exact":#claim last bid was exact
				pass

			case "call":#claim last bid was wrong
				pass

			case "none":#out of game, do nothing
				pass 
	

	def listen(self, **kwargs):
		
		match kwargs.signal_type:
			case "take action":
				self.chooseAction([kwargs.die_face, kwargs.number])
	

	def chooseAction(self, bid: list):
		#bid=[die face, number bid]

	
	def _calculateEstimatedNumber(die_face: int, assumed_number: int, assumed_unknown: int):
		if self.one_die_round or die_face == 1:
			pass


	def _diceProbabilities(bid: list) -> list:
		blind_prob = []