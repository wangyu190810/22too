
# mongo学习

```javascript 

db.accounts.insert([
    {
        name:"jack",
        balance:2000,
        contact: ["111111111","Alabama","US"],
    },
    {
        name:"kanran",
        balance: 25000,
        contact:[["222222","3333333"],"Beijing","China"]
    }
])

db.accounts.find( { contact: { $all: ["China", "Beijing"] } } )

db.accounts.find( { contact: { $all:[ ["222222","3333333"] ] } } )

db.accounts.find( { balance: { $elemMatch:{ $gt: "222221",$lt: "33333334" } } } )


db.accounts.insert(
    {
        name:"charlie",
        balance:1000
    }
)

db.accounts.find({name:{$regex:/LIE/, $options:'i'}})

var myCursor = db.accounts.find()

// 只能取一个，这里是一个迭代器，使用遍历或者小标，一种方式。

myCursor
myCursor[1]

var myCursor = db.accounts.find().noCursorTimeOut()
// 需要主动关注

myCursor.close()


var myCursor = db.accounts.find({name:"wangyu"})
while(myCursor.hasNext()){
    printjson(myCursor.next())
}
// 判断下一个节点，然后打印

var myCursor = db.accounts.find({name:"wangyu"})
myCursor.forEach(printjson)

// 也可以私用foreach

var myCursor = db.accounts.find().limit(1)
var myCursor = db.accounts.find().skip(1)
// limit 返回多少  skip 跳过多少

db.accounts.find().count()
db.accounts.find().limit(1).count()
db.accounts.find().limit(1).count(true)


db.accounts.find().limit(2).skip(1)
db.accounts.find().sort({name:-1}).limit(1).skip(1)

db.accounts.find(
    {contact:{$gt:"Alabama"}},
    {_id:0,name:1,"contact.$":1}
)

```

