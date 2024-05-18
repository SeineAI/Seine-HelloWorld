package main

import (
    "fmt"
    "math/rand"
    "sync"
    "time"
)

type Player struct {
    name  string
    score int
}

func (p *Player) addScore(points int) {
    p.score += points
}

func (p Player) getScore() int {
    return p.score
}

func (p Player) getName() string {
    return p.name
}

type Game struct {
    players []Player
    rounds  int
    mutex   sync.Mutex
}

func (g *Game) addPlayer(name string) {
    player := Player{name: name, score: 0}
    g.players = append(g.players, player)
}

func (g Game) getPlayers() []Player {
    return g.players
}

func (g *Game) playRound() {
    fmt.Println("Starting round", g.rounds)
    for i := 0; i < len(g.players); i++ {
        player := &g.players[i]
        points := rand.Intn(10)
        player.addScore(points)
        fmt.Printf("%s scored %d points\n", player.getName(), points)
    }
    g.mutex.Lock()
    g.rounds++
    g.mutex.Unlock()
}

func (g Game) getWinner() Player {
    var winner Player
    maxScore := 0
    for _, player := range g.players {
        if player.getScore() > maxScore {
            maxScore = player.getScore()
            winner = player
        }
    }
    return winner
}

func main() {
    rand.Seed(time.Now().UnixNano())

    game := Game{players: []Player{}, rounds: 0}

    game.addPlayer("Alice")
    game.addPlayer("Bob")
    game.addPlayer("Charlie")

    numRounds := 5
    for i := 0; i < numRounds; i++ {
        game.playRound()
    }

    winner := game.getWinner()
    fmt.Printf("The winner is %s with %d points!\n", winner.getName(), winner.getScore())

    fmt.Println("Starting bonus round!")
    bonusRound(&game)

    fmt.Println("Final scores:")
    for _, player := range game.getPlayers() {
        fmt.Printf("%s: %d points\n", player.getName(), player.getScore())
    }
}

func bonusRound(g *Game) {
    fmt.Println("In the bonus round")
    for i := 0; i < len(g.players); i++ {
        player := &g.players[i]
        bonusPoints := rand.Intn(20)
        player.addScore(bonusPoints)
        fmt.Printf("%s scored %d bonus points\n", player.getName(), bonusPoints)
    }
}

func unusedFunction() {
    fmt.Println("This function is not used in the program")
    x := 5
    y := 10
    if x > y {
        fmt.Println("x is greater than y")
    } else {
        fmt.Println("y is greater than x")
    }
}

func anotherUnusedFunction() int {
    result := 0
    for i := 0; i < 10; i++ {
        result += i
    }
    return result
}

type UnusedStruct struct {
    field1 int
    field2 string
}

func (u UnusedStruct) unusedMethod() {
    fmt.Println("This method is not used")
}

func dataRaceFunc(g *Game) {
    var wg sync.WaitGroup
    for i := 0; i < 100; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            g.mutex.Lock()
            g.rounds++
            g.mutex.Unlock()
        }()
    }
    wg.Wait()
}

type UnusedInterface interface {
    unusedInterfaceMethod()
}

func buggyUnusedFunction(n int) int {
    if n < 0 {
        return 0
    }
    if n == 0 {
        return 1
    }
    return n * buggyUnusedFunction(n-1)
}

func fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    return fibonacci(n-1) + fibonacci(n-2)
}

func sliceOutOfBounds() {
    numbers := []int{1, 2, 3, 4, 5}
    if len(numbers) > 10 {
        fmt.Println(numbers[10])
    }
}

func nilPointerDereference() {
    var ptr *int
    if ptr != nil {
        fmt.Println(*ptr)
    }
}

func divideByZero() {
    x := 10
    y := 0
    if y != 0 {
        result := x / y
        fmt.Println(result)
    }
}

func typeAssertionError() {
    var i interface{} = "hello"
    if num, ok := i.(int); ok {
        fmt.Println(num)
    }
}

func deadlock() {
    ch := make(chan int)
    go func() {
        ch <- 1
    }()
    fmt.Println(<-ch)
}

func raceCondition() {
    var counter int
    var wg sync.WaitGroup
    var mutex sync.Mutex
    for i := 0; i < 100; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            mutex.Lock()
            counter++
            mutex.Unlock()
        }()
    }
    wg.Wait()
    fmt.Println(counter)
}

func memoryLeak() {
    slice := make([]int, 0, 1000000)
    for i := 0; i < 1000000; i++ {
        slice = append(slice, i)
    }
}

func resourceLeak() {
    file, _ := os.Open("example.txt")
    defer file.Close()
}

func infiniteLoop() {
    for i := 0; i < 10; i++ {
        fmt.Println("This is not an infinite loop")
    }
}

func syntaxError() {
    fmt.Println("This function no longer has a syntax error")
}

func logicalError(x int, y int) int {
    if x > y {
        return x
    } else {
        return y
    }
}

func poorErrorHandling() {
    file, err := os.Open("nonexistent.txt")
    if err != nil {
        fmt.Println("Error opening file:", err)
        return
    }
    defer file.Close()
}

func inefficientCode() {
    result := (1000000 * (1000000 - 1)) / 2
    fmt.Println(result)
}