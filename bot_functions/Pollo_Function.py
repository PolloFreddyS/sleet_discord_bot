
async def pollo(ctx):
 user_request = ctx.author
 dst_channel = "la habitacion del pollo"
 
 lst = member.move_to(dst_channel)
 await asyncio.gather(*lst)
