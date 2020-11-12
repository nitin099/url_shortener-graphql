import graphene

import shortener.schema


class Query(shortener.schema.Query, graphene.ObjectType):
    import pdb; pdb.set_trace()  # breakpoint 56ce3fbb //
    pass


class Mutation(shortener.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
