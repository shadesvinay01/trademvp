class InfluencerScore:

    def credibility(self, followers, engagement):

        follower_score = min(40, followers / 1_000_000 * 40)

        engagement_score = min(30, engagement)

        return follower_score + engagement_score
