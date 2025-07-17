class JobRole:
    def __init__ (self,domain, position, experience, tech_needed):
        self.domain = domain
        self.position= position
        self.experience= experience
        self.tech_needed = tech_needed

    def __str__(self):
        return f"{self.domain} | {self.position} | {self.experience} | {self.tech_needed}"
    
    def to_dict(self):
        return { "domain": self.domain,
                "position": self.position,
                "experience": self.experience,
                "tech_needed": self.tech_needed
                  }
    
    @staticmethod
    def from_dict(data):
        return JobRole(
        domain= data["domain"],
        position= data["position"],
        experience= data["experience"],
        tech_needed= data["tech_needed"]
        )

        
        
        