from game.entities import Community


class CommunityService:
    def start_new_community(self) -> Community:
        community = Community()
        return community
