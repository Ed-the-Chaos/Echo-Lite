class AdaptiveKnowledgeRefinement:
    def __init__(self):
        self.knowledge_base = {}  # Stores key insights
        self.refinement_log = []  # Tracks refinements

    def add_knowledge(self, key, information):
        """Adds new knowledge or updates existing knowledge dynamically."""
        if key in self.knowledge_base:
            self.refinement_log.append(f"Refined: {key}")
        else:
            self.refinement_log.append(f"Added: {key}")
        self.knowledge_base[key] = information

    def detect_inconsistencies(self, key, new_information):
        """Detects if new information contradicts existing knowledge."""
        if key in self.knowledge_base and self.knowledge_base[key] != new_information:
            self.refinement_log.append(f"Inconsistency found in {key}")
            return True
        return False

    def refine_knowledge(self, key, new_information):
        """Refines knowledge by resolving contradictions or improving details."""
        if self.detect_inconsistencies(key, new_information):
            self.knowledge_base[key] = new_information
            self.refinement_log.append(f"Resolved inconsistency in {key}")
        else:
            self.add_knowledge(key, new_information)

    def show_knowledge(self):
        """Displays stored knowledge."""
        return self.knowledge_base

    def show_refinement_log(self):
        """Displays all refinements made to knowledge."""
        return self.refinement_log

# Example Usage (to be removed when integrated)
if __name__ == "__main__":
    akr = AdaptiveKnowledgeRefinement()
    akr.add_knowledge("AI", "Artificial Intelligence is evolving.")
    akr.refine_knowledge("AI", "AI is evolving through reinforcement learning.")
    print(akr.show_knowledge())
    print(akr.show_refinement_log())
